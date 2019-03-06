package com.example.vitarun;

import com.google.gson.Gson;

import java.io.IOException;
import java.util.HashMap;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class ServerComms {

    static String url = "http://146.169.147.94:3000";
    Gson gson;
    OkHttpClient client;

    public ServerComms()
    {
        client = new OkHttpClient();
        gson = new Gson();
    }

    public void GetFeature(final String featureName)
    {
        final String featureReturn = new String();

        Request request = new Request.Builder()
                .url(url)
                .addHeader("Feature", featureName)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (response.isSuccessful())
                {
                    String myResponse = response.body().string();
//                    featureReturn = myResponse;

                }
            }
        });

//        return response;
    }

    public void PostPressureData(HashMap<Integer, String> data)
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
}
