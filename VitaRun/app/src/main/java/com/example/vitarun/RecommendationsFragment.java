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
import android.widget.ViewSwitcher;

import com.google.gson.Gson;


/**
 * A simple {@link Fragment} subclass.
 */
public class RecommendationsFragment extends Fragment {

    Gson gson = new Gson();

    TextView tv;
    TextView tv2;
    TextView tv3;




    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
       View RootView = inflater.inflate(R.layout.fragment_recommendations, container, false);

        String requestfromserver = "{'type': 1, 'freq': 150, 'totalNum': 73}";


        tv = (TextView)RootView.findViewById(R.id.firstrecom_body);
        tv2 = (TextView)RootView.findViewById(R.id.secondrecom_body);
        tv3 = (TextView)RootView.findViewById(R.id.thirdrecom_body);

        updaterecomText(requestfromserver);

//        Summary_recom summary_recom = gson.fromJson(request , Summary_recom.class);
//        System.out.println(summary_recom.type);
//        System.out.println(summary_recom.freq);
//        System.out.println(summary_recom.totalNum);


//
//        switch (summary_recom.type) {
//            case "0":
//                tv.setText("Normal Pronation");
//                break;
//            case "1":
//                tv.setText("UnderPronation");
//                break;
//            case "2":
//                tv.setText("OverPronation");
//                break;
//        }

//        float freq = Float.parseFloat(summary_recom.freq);
//        String Stridefreq1  = "Your current stride frequency is equal to ";
//        String Stridefreq2  = " steps per min. You should ";
//
//        if (freq > 180){
//            String Stridefreq3  = "try running with smaller steps!";
//            String FinalStridefreq1  = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
////            System.out.println(FinalStridefreq1);
//            tv2.setText(FinalStridefreq1);
//        }
//
//        if (freq < 180){
//            String Stridefreq3  = "try running with larger steps!";
//            String FinalStridefreq1  = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
////            System.out.println(FinalStridefreq1);
//            tv2.setText(FinalStridefreq1);
//        }
//
//        if (freq == 180){
//            String Stridefreq3  = "keep the same pace!";
//            String FinalStridefreq1  = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
////            System.out.println(FinalStridefreq1);
//            tv2.setText(FinalStridefreq1);
//        }
//
//        String TotalNbsteps1  = "You have run ";
//        String TotalNbsteps2  = " steps so far!";
//        String FinalTotalNbsteps  = TotalNbsteps1 + summary_recom.totalNum + TotalNbsteps2;
//        tv3.setText(FinalTotalNbsteps);



//
        return RootView;
    }


    public void updaterecomText(String string){

        Summary_recom summary_recom = gson.fromJson(string , Summary_recom.class);
        System.out.println(summary_recom.type);
        System.out.println(summary_recom.freq);
        System.out.println(summary_recom.totalNum);

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

        float freq = Float.parseFloat(summary_recom.freq);
        String Stridefreq1  = "Your current stride frequency is equal to ";
        String Stridefreq2  = " steps per min. You should ";

        if (freq > 180){
            String Stridefreq3  = "try running with smaller steps!";
            String FinalStridefreq1  = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
//            System.out.println(FinalStridefreq1);
            tv2.setText(FinalStridefreq1);
        }

        if (freq < 180){
            String Stridefreq3  = "try running with larger steps!";
            String FinalStridefreq1  = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
//            System.out.println(FinalStridefreq1);
            tv2.setText(FinalStridefreq1);
        }

        if (freq == 180){
            String Stridefreq3  = "keep the same pace!";
            String FinalStridefreq1  = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
//            System.out.println(FinalStridefreq1);
            tv2.setText(FinalStridefreq1);
        }

        String TotalNbsteps1  = "You have run ";
        String TotalNbsteps2  = " steps so far!";
        String FinalTotalNbsteps  = TotalNbsteps1 + summary_recom.totalNum + TotalNbsteps2;
        tv3.setText(FinalTotalNbsteps);

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

