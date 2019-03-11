package com.example.vitarun;


import android.content.Context;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.google.gson.Gson;


/**
 * A simple {@link Fragment} subclass.
 */
public class RecommendationsFragment extends Fragment {

    Gson gson = new Gson();





    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
       View RootView = inflater.inflate(R.layout.fragment_recommendations, container, false);

        String request = "{'type': 1, 'freq': 180, 'totalNum': 73}";


        TextView tv = (TextView)RootView.findViewById(R.id.firstrecom_body);


        Summary_recom summary_recom = gson.fromJson(request , Summary_recom.class);
        System.out.println(summary_recom.type);



        switch (summary_recom.type) {
            case "0":
                tv.setText("Normal Pronation");
                break;
            case "1":
                tv.setText("UnderPronation");
                break;
            case "2":
                tv.setText("OverPronation");
                break;
        }

//
        return RootView;
    }

    private class Summary_recom {
        public String type;
        public String freq;
        public String totalNum;

        public Summary_recom(String type, String freq, String totalNum) {
            this.type = type;
            this.freq = freq;
            this.totalNum = totalNum;
        }
    }



}

