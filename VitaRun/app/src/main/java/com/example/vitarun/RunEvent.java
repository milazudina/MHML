package com.example.vitarun;

import android.content.Context;
import android.content.SharedPreferences;
import android.util.Log;
import android.util.Pair;

import com.google.gson.Gson;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.channels.FileLock;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

import static android.content.Context.MODE_PRIVATE;

public class RunEvent {

    private LocalDateTime startTime;
    private LocalDateTime endTime;

    ArrayList<Pair<String, Float[]>> DATA_BUFFER;

    static int dataBufferLength = 128;
    ServerComms serverComms;

    ArrayList<Float[]> dataSet;
    int dataIndex;

    Gson gson;
    private Context context;

    public boolean paused;

    final DateTimeFormatter dateFormat;

    public RunEvent(Context current) {
        System.out.println("Run Event Created");
        this.context = current;

        serverComms = new ServerComms();
        DATA_BUFFER = new ArrayList<>();

        dateFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss.S");

        InputStream inputStream = context.getResources().openRawResource(R.raw.mockdata);
        CSVFile csvFile = new CSVFile(inputStream);
        dataSet = csvFile.read();

        dataIndex = 0;
        gson = new Gson();
    }


    public void addDataSample(String side, byte[] dataSample) {
//        DATA_BUFFER.add(dataSample);

        LocalDateTime currTimeDT = LocalDateTime.now(ZoneId.systemDefault());
        String currTime = currTimeDT.format(dateFormat);
        System.out.println(side + "Data Sample Added");

        DATA_BUFFER.add(new Pair(currTime, (dataSet.get(dataIndex))));


        if (DATA_BUFFER.size() == dataBufferLength) {

            serverComms.PostPressureData(DATA_BUFFER);

            String jsonString = gson.toJson(DATA_BUFFER);

//            writeToFile(jsonString, context);
            System.out.println(jsonString);

            DATA_BUFFER.clear();
        }

        dataIndex += 1;
    }

    public void RefreshFeatures() {
        //Make get request.

        // Store result.

        // Call recommendations fragment update text method
    }

    private void writeToFile(String data, Context context) {
        try {
            OutputStreamWriter outputStreamWriter = new OutputStreamWriter(context.openFileOutput("data.txt", Context.MODE_PRIVATE));
            outputStreamWriter.write(data);
            outputStreamWriter.close();
        } catch (IOException e) {
            Log.e("Exception", "File write failed: " + e.toString());
        }
    }

    public void StartRunEvent() {
        System.out.println("Run Started");
        serverComms.getFeature("startRun");
        startTime = LocalDateTime.now(ZoneId.systemDefault());
    }

    public void PauseRunEvent() {
        this.paused = true;
        System.out.println("Run Paused");
    }


    public void EndRunEvent() {
        endTime = LocalDateTime.now(ZoneId.systemDefault());
        System.out.println("Run Ended");

    }

    public Duration getEllapsedTime() {
        return Duration.between(startTime, ZonedDateTime.now(ZoneId.systemDefault()));
    }

    public LocalDateTime getStartTime() {
        return startTime;
    }


    public class CSVFile {
        InputStream inputStream;

        public CSVFile(InputStream inputStream) {
            this.inputStream = inputStream;
        }

        public ArrayList<Float[]> read() {
            ArrayList<Float[]> resultList = new ArrayList<>();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
            try {
                String csvLine;
                while ((csvLine = reader.readLine()) != null) {
                    String[] row = csvLine.split(",");

                    Float[] parsed = new Float[row.length];
                    for (int i = 0; i < row.length; i++) {

                        try {
                            parsed[i] = Float.valueOf(row[i] + "f");
                        } catch (NumberFormatException e) {
                            parsed[i] = 0f;
                        }
                    }
                    resultList.add(parsed);
                }
            } catch (IOException ex) {
                throw new RuntimeException("Error in reading CSV file: " + ex);
            } finally {
                try {
                    inputStream.close();
                } catch (IOException e) {
                    throw new RuntimeException("Error while closing input stream: " + e);
                }
            }
            return resultList;
        }
    }
}
