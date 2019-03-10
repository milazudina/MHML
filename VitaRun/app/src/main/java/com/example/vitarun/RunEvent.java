package com.example.vitarun;

import android.content.Context;
import android.content.SharedPreferences;
import android.util.Log;

import com.google.gson.Gson;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.time.Duration;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

import static android.content.Context.MODE_PRIVATE;

public class RunEvent {

    private ZonedDateTime startTime;
    private ZonedDateTime endTime;

    HashMap<String, double[]> DATA_BUFFER;

    static int dataBufferLength = 128;
    ServerComms serverComms;

    ArrayList<double[]> dataSet;
    int dataIndex;

    Gson gson;
    private Context context;

    public RunEvent(Context current)
    {
        System.out.println("Run Event Created");
        this.context = current;

        serverComms = new ServerComms();
        DATA_BUFFER = new HashMap<>();

        InputStream inputStream = context.getResources().openRawResource(R.raw.mockdata);
        CSVFile csvFile = new CSVFile(inputStream);
        dataSet = csvFile.read();

        dataIndex = 0;
        gson = new Gson();
    }


    public void addDataSample(String side, byte[] dataSample)
    {
//        DATA_BUFFER.add(dataSample);

        ZonedDateTime currZDTime = ZonedDateTime.now(ZoneId.systemDefault());
        String currTime = currZDTime.toString();
        System.out.println(side + "Data Sample Added");

        DATA_BUFFER.put(currTime, dataSet.get(dataIndex));


        if (DATA_BUFFER.size() == dataBufferLength)
        {
            serverComms.PostPressureData(DATA_BUFFER);

            String jsonString = gson.toJson(DATA_BUFFER);

            writeToFile(jsonString, context);
            System.out.println(jsonString);

            DATA_BUFFER.clear();
        }

        dataIndex += 1;

    }

    private void writeToFile(String data,Context context) {
        try {
            OutputStreamWriter outputStreamWriter = new OutputStreamWriter(context.openFileOutput("data.txt", Context.MODE_PRIVATE));
            outputStreamWriter.write(data);
            outputStreamWriter.close();
        }
        catch (IOException e) {
            Log.e("Exception", "File write failed: " + e.toString());
        }
    }

    public void StartRunEvent()
    {
        startTime = ZonedDateTime.now(ZoneId.systemDefault());
    }

    public void PauseRunEvent()
    {

    }


    public void EndRunEvent()
    {
        endTime = ZonedDateTime.now(ZoneId.systemDefault());

    }

    public Duration getEllapsedTime()
    {
        return Duration.between(startTime, ZonedDateTime.now(ZoneId.systemDefault()));
    }

    public ZonedDateTime getStartTime()
    {
        return startTime;
    }



    public class CSVFile {
        InputStream inputStream;

        public CSVFile(InputStream inputStream){
            this.inputStream = inputStream;
        }

        public ArrayList<double[]> read(){
            ArrayList<double[]> resultList = new ArrayList<>();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
            try {
                String csvLine;
                while ((csvLine = reader.readLine()) != null) {
                    String[] row = csvLine.split(",");

                    double[] parsed = new double[row.length];
                    for (int i = 0; i<row.length; i++) parsed[i] = Double.valueOf(row[i]);

                    resultList.add(parsed);
                }
            }
            catch (IOException ex) {
                throw new RuntimeException("Error in reading CSV file: "+ex);
            }
            finally {
                try {
                    inputStream.close();
                }
                catch (IOException e) {
                    throw new RuntimeException("Error while closing input stream: "+e);
                }
            }
            return resultList;
        }
    }
}
