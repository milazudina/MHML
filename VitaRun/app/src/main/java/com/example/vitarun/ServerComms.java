package com.example.vitarun;

import com.google.gson.Gson;

import java.io.IOException;
import java.util.Date;
import java.util.HashMap;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class ServerComms {

    // ip address of server machine + port.
    static String url = "http://146.169.147.94:3000";

    Gson gson;
    OkHttpClient client;

    public ServerComms()
    {
        // HTTP Client.
        client = new OkHttpClient();

        // GSON object converts Java types into JSON string format.
        gson = new Gson();
    }

    // Method to set user database on server side.
    public void SetUser()
    {

    }

    public String GetFeature(final String featureName)
    {
        // SyncResult object allows string returned from the GET request to be assigned
        // asyncronously.
        final SyncResult syncResult = new SyncResult();

        // Add featureName to header of request.
        Request request = new Request.Builder()
                .url(url)
                .addHeader("Feature", featureName)
                .build();

        client.newCall(request).enqueue(new Callback() {

            String myResponse;

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (response.isSuccessful())
                {
                    // Assign body of response to returned value.
                    myResponse = response.body().string();
                    syncResult.setResult(myResponse);
                }
            }
        });

        return syncResult.getResult();
    }

    public void PostPressureData(HashMap<Date, String> data)
    {
        OkHttpClient client = new OkHttpClient();
        MediaType JSON = MediaType.parse("application/json; charset=utf-8");

        // Convert data to JSON Format.
        String json = gson.toJson(data);

        // Add JSON to body of posted request.
        RequestBody body = RequestBody.create(JSON, json);

        Request request = new Request.Builder()
                .url(url)
                .post(body)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                System.out.println(response.body().string());
            }
        });
    }

    public class SyncResult {
        private static final long TIMEOUT = 20000L;
        private String result;

        public String getResult() {
            long startTimeMillis = System.currentTimeMillis();
            while (result == null && System.currentTimeMillis() - startTimeMillis < TIMEOUT) {
                synchronized (this) {
                    try {
                        wait(TIMEOUT);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }
            return result;
        }

        public void setResult(String result) {
            this.result = result;
            synchronized (this) {
                notify();
            }
        }
    }
}
