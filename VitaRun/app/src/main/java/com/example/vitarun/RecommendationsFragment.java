package com.example.vitarun;


import android.content.Context;
import android.content.Intent;
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

    TextView tv4;
    TextView tv5;
    TextView tv6;

    public ViewSwitcher mViewSwitcher;

    Intent speechIntent;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
       View RootView = inflater.inflate(R.layout.fragment_recommendations, container, false);

        String requestfromserver1 = "{'type': 1, 'freq': 174, 'totalNum': 73}";
        String requestfromserver2 = "{'type': 2, 'freq': 150, 'totalNum': 103}";


        tv = (TextView)RootView.findViewById(R.id.firstrecom_body);
        tv2 = (TextView)RootView.findViewById(R.id.secondrecom_body);
        tv3 = (TextView)RootView.findViewById(R.id.thirdrecom_body);

        tv4 = (TextView)RootView.findViewById(R.id.firstsum_body);
        tv5 = (TextView)RootView.findViewById(R.id.secondsum_body);
        tv6 = (TextView)RootView.findViewById(R.id.thirdsum_body);

        mViewSwitcher = (ViewSwitcher) RootView.findViewById(R.id.recomswitcher);
        mViewSwitcher.showNext();
        mViewSwitcher.reset();

//        updaterecomText(requestfromserver1);
//        updaterecomText2(requestfromserver2);

        speechIntent = new Intent(getActivity(), TextToSpeechService.class);

        return RootView;
    }

    public void AudioFeedback(String features)
    {

        final Summary_recom summary_recom = gson.fromJson(features , Summary_recom.class);

        float freq = Float.parseFloat(summary_recom.freq);

        String Stridefreq3 =" ";

        if (freq > 195) {
            Stridefreq3 = "Are you sprinting? You should SLOW DOWNNNN, mate!";
        }


        else if (185 < freq && freq < 195) {
            Stridefreq3 = "WOW!! You are running at elite runners' stride rate!";
        }

        else if (165 <= freq && freq <= 175) {
            Stridefreq3 = "You are just under the perfect running pace, try taking smaller steps and reducing ground contact time!";
        }

        else if (freq < 165) {
            Stridefreq3 = "Try taking smaller steps and reducing ground contact time!";
            //            System.out.println(FinalStridefreq1);
        }

        else if (175 < freq && freq < 185) {
            Stridefreq3 = "Well done! Keep the same pace.";
            //            System.out.println(FinalStridefreq1);
        }


        speechIntent.putExtra(TextToSpeechService.EXTRA_WORD, Stridefreq3);

        System.out.println("Speaking");

        getActivity().startService(speechIntent);

    }


    public void updaterecomText(String string){

        final Summary_recom summary_recom = gson.fromJson(string , Summary_recom.class);
        System.out.println(summary_recom.type);
        System.out.println(summary_recom.freq);
        System.out.println(summary_recom.totalNum);

        getActivity().runOnUiThread(new Runnable() {

            @Override
            public void run() {

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
                String Stridefreq1 = "Your current stride frequency is ";
                String Stridefreq2 = " steps per minute. ";

                if (freq > 195) {
                    String Stridefreq3 = "Are you sprinting? You should SLOW DOWNNNN, mate!";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
                    //            System.out.println(FinalStridefreq1);
                    tv2.setText(FinalStridefreq1);
                }

                if (185 < freq && freq < 195) {
                    String Stridefreq3 = "You are running at elite runners' stride rate!";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
                    //            System.out.println(FinalStridefreq1);
                    tv2.setText(FinalStridefreq1);
                }

                if (165 <= freq && freq <= 175) {
                    String Stridefreq3 = "Take smaller steps & reduce ground contact time!";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
                    //            System.out.println(FinalStridefreq1);
                    tv2.setText(FinalStridefreq1);
                }

                if (freq < 165) {
                    String Stridefreq3 = "Take smaller steps & reduce ground contact time!";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
                    //            System.out.println(FinalStridefreq1);
                    tv2.setText(FinalStridefreq1);
                }

                if (175 < freq && freq < 185) {
                    String Stridefreq3 = "Well done! Keep the same pace.";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
                    //            System.out.println(FinalStridefreq1);
                    tv2.setText(FinalStridefreq1);
                }


                String TotalNbsteps2 = " steps overall!";
                String FinalTotalNbsteps = summary_recom.totalNum + TotalNbsteps2;
                tv3.setText(FinalTotalNbsteps);
            }
        });
    }



    public void updaterecomText2(String string){

        final Summary_recom summary_recom = gson.fromJson(string , Summary_recom.class);
        System.out.println(summary_recom.type);
        System.out.println(summary_recom.freq);
        System.out.println(summary_recom.totalNum);

        getActivity().runOnUiThread(new Runnable() {
            @Override
            public void run() {

                switch (summary_recom.type) {
                    case "0":
                        tv4.setText("You have Normal Pronation");
                        break;
                    case "1":
                        tv4.setText("You are UnderPronating");
                        break;
                    case "2":
                        tv4.setText("You are OverPronating");
                        break;
                }

                float freq = Float.parseFloat(summary_recom.freq);
                String Stridefreq1 = "Your average stride frequency is ";
                String Stridefreq2 = " steps per minute. ";

                if (freq > 195) {
                    String Stridefreq3 = "Are you always late? Your average pace is too rapid, SLOW DOWNN, mate! ";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
//            System.out.println(FinalStridefreq1);
                    tv5.setText(FinalStridefreq1);
                }

                if (185 < freq && freq < 195) {
                    String Stridefreq3 = "WOW!! You are running at elite runners' stride rate!";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
//            System.out.println(FinalStridefreq1);
                    tv5.setText(FinalStridefreq1);
                }

                if (165 < freq && freq < 175) {
                    String Stridefreq3 = "Your average is close to the perfect running pace.";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
//            System.out.println(FinalStridefreq1);
                    tv5.setText(FinalStridefreq1);
                }

                if (freq < 165) {
                    String Stridefreq3 = "Try taking smaller steps and reducing ground contact time!";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
//            System.out.println(FinalStridefreq1);
                    tv5.setText(FinalStridefreq1);
                }

                if (175 < freq && freq < 185) {
                    String Stridefreq3 = "Well done! Your pace is perfect.";
                    String FinalStridefreq1 = Stridefreq1 + summary_recom.freq + Stridefreq2 + Stridefreq3;
//            System.out.println(FinalStridefreq1);
                    tv5.setText(FinalStridefreq1);
                }

                String TotalNbsteps1 = "You have run ";
                String TotalNbsteps2 = " steps so far!";
                String FinalTotalNbsteps = TotalNbsteps1 + summary_recom.totalNum + TotalNbsteps2;
                tv6.setText(FinalTotalNbsteps);
            }
    });
    }


    private class Summary_recom {
        public String type;
        public String freq;
        public String totalNum;

        public Summary_recom(String type, String freq, String totalNum) {
            this.type = type;
            this.freq = freq.substring(0, 2);
            this.totalNum = totalNum;
        }
    }



}

