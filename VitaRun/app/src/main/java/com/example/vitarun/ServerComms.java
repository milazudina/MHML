package com.example.vitarun;

import android.renderscript.Sampler;
import android.util.Pair;

import com.google.gson.Gson;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.LinkedHashMap;
import java.util.Map;
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
    static String url = "http://146.169.189.71:3000";

    Gson gson;
    OkHttpClient client;

    public ServerComms()
    {
        // HTTP Client.
        client = new OkHttpClient();

        // GSON object converts Java types into JSON string format.
        gson = new Gson();
    }

    public String CheckConnection()
    {
        final SyncResult syncResult = new SyncResult();

        Request request = new Request.Builder()
                .url(url)
                .addHeader("ConnectionCheck", "")
                .build();

        client.newCall(request).enqueue(new Callback() {

            String myResponse;

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (response.isSuccessful()) {
                    syncResult.setResult("1");
                } else {
                    syncResult.setResult("0");
                }
            }
        });

        return syncResult.getResult();
    }

    // Method to set user database on server side.
    public int login(String userName, String password)
    {
        final SyncResult syncResult = new SyncResult();
        Map<String, String> table = new Hashtable<>();
        table.put("username", userName);
        table.put("password", password);
        String json = gson.toJson(table);
        //String header = String.format("login : , %s : %s", userName,password);

        // Add featureName to header of request.
        Request request = new Request.Builder()
                .url(url)
                .addHeader("login", json)
                .build();

        client.newCall(request).enqueue(new Callback() {

            String myResponse;

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (response.isSuccessful()) {
                    // Assign body of response to returned value.
                    myResponse = response.body().string();
                    syncResult.setResult(myResponse);
                }
            }
        });


        try {
            if (Boolean.parseBoolean(syncResult.getResult())){
                return 1;

            }else{
                return 0;
        }
        }catch(Exception e){
            System.out.print("Non-boolean response to login GET request");
            return -1;
        }
    }
    public boolean createProfile(String userName, String password, String name, int Age, int weight)
    {
        final SyncResult syncResult = new SyncResult();
        User user = new User(userName, password, name, Age, weight);
        String json = gson.toJson(user);
        //String header = String.format("login : , %s : %s", userName,password);

        // Add featureName to header of request.
        System.out.println(json);
        Request request = new Request.Builder()
                .url(url)
                .addHeader("createProfile", json)
                .build();

        client.newCall(request).enqueue(new Callback() {

            String myResponse;

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (response.isSuccessful()) {
                    // Assign body of response to returned value.
                    myResponse = response.body().string();
                    syncResult.setResult(myResponse);
                }
            }
        });


        try {
            return  Boolean.parseBoolean(syncResult.getResult());
        }catch(Exception e){
            System.out.print("Non-boolean response to createProfile GET request");
            return false;
        }
    }


    public void setUserDetails(Object user)
    {
        final SyncResult syncResult = new SyncResult();
        String json = gson.toJson(user);
        //String header = String.format("login : , %s : %s", userName,password);

        // Add featureName to header of request.
        System.out.println(json);
        Request request = new Request.Builder()
                .url(url)
                .addHeader("setUserDetails", json)
                .build();

        client.newCall(request).enqueue(new Callback() {

            String myResponse;

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (response.isSuccessful()) {
                    // Assign body of response to returned value.
                    myResponse = response.body().string();
                    syncResult.setResult(myResponse);
                }
            }
        });

    }


    public  User getUserDetails(String username)
    {
        final SyncResult syncResult = new SyncResult();


        Request request = new Request.Builder()
                .url(url)
                .addHeader("getUserDetails", username)
                .build();
        client.newCall(request).enqueue((new Callback() {

            String myResponse;

            @Override
            public void onFailure(Call call, IOException e) {e.printStackTrace();}

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (response.isSuccessful()){
                    myResponse = response.body().string();
                    syncResult.setResult(myResponse);

                }

            }
        }));

        String result = syncResult.getResult();
        System.out.println("Json Result"+result);

        User user = gson.fromJson(result, User.class);
        System.out.println("Received: Name:"+user.name+" Username:"+user.username+" Age:"+user.age+" Weight"+user.weight);
        return user;
    }

    public String getFeature(final String featureName)
    {
        // SyncResult object allows string returned from the GET request to be assigned
        // asyncronously.
        final SyncResult syncResult = new SyncResult();

        // Add featureName to header of request.
        Request request = new Request.Builder()
                .url(url)
                .addHeader(featureName, "")
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

    public String getFeature(final String featureName, final String Details)
    {
        // SyncResult object allows string returned from the GET request to be assigned
        // asyncronously.
        final SyncResult syncResult = new SyncResult();

        // Add featureName to header of request.
        Request request = new Request.Builder()
                .url(url)
                .addHeader(featureName, Details)
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

    public boolean PostPressureData(LinkedHashMap<Integer, Float[]> data)
    {
        OkHttpClient client = new OkHttpClient();
        MediaType JSON = MediaType.parse("application/json; charset=utf-8");

        final SyncResult syncResult = new SyncResult();

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
                syncResult.setResult(response.body().toString());
            }
        });

        boolean r = false;

        switch (syncResult.getResult())
        {
            case "True":
                r = true;
                break;
        }

        return r;
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
