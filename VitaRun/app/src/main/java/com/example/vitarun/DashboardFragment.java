package com.example.vitarun;

import android.app.ActionBar;
import android.graphics.Color;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.JsonReader;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.anychart.anychart.AnyChart;
import com.anychart.anychart.AnyChartView;
import com.anychart.anychart.DataEntry;
import com.anychart.anychart.Pie;
import com.anychart.anychart.ValueDataEntry;
import com.github.mikephil.charting.charts.BarChart;
import com.github.mikephil.charting.components.Legend;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.data.BarData;
import com.github.mikephil.charting.data.BarDataSet;
import com.github.mikephil.charting.data.BarEntry;
import com.github.mikephil.charting.formatter.IndexAxisValueFormatter;
import com.github.mikephil.charting.utils.ColorTemplate;
import com.github.sundeepk.compactcalendarview.CompactCalendarView;
import com.github.sundeepk.compactcalendarview.domain.Event;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.series.BarGraphSeries;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.StringReader;
import java.lang.reflect.Array;
import java.sql.Timestamp;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;


public class DashboardFragment extends Fragment {

    ServerComms serverComms;
    Gson gson = new Gson();
    DateFormat formatter;



    DateFormat dateFormat = new SimpleDateFormat("YYYY-mm-dd HH:MM:SS");



    static String jsonString = "{'DictA' : {\"Datetime_Start\": \"2019-03-09 12:41:24\",\"Datetime_Stop\":\"2019-03-09 12:50:24\",\"Number_Of_Steps\": \"100\",\"Count_NP\": \"20\",\"Count_OP\": \"40\",\"Count_UP\":\"40\",\"Average_Frequency\": \"3\"}, 'DictB' : {\"Datetime_Start\": \"2019-03-08 12:41:24\",\"Datetime_Stop\": \"2019-03-08 12:50:24\",\"Number_Of_Steps\": \"100\",\"Count_NP\": \"20\",\"Count_OP\": \"40\",\"Count_UP\":\"\"40\",\"Average_Frequency\": \"3\"}}";

    String jsonString2 = "{\"Datetime_Start\": \"2019-03-09 12:41:24\",\"Datetime_Stop\":\"2019-03-09 12:50:24\",\"Number_Of_Steps\": \"100\",\"Count_NP\": \"20\",\"Count_OP\": \"40\",\"Count_UP\": \"40\",\"Average_Frequency\": \"3\"}";


    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_dashboard, container, false);
        final CompactCalendarView compactCalendarView = (CompactCalendarView) view.findViewById(R.id.compactcalendar_view);
        final SimpleDateFormat dateFormatForMonth = new SimpleDateFormat("MMM - yyyy", Locale.getDefault());
        final TextView monthTextView = (TextView) view.findViewById(R.id.Month_title);
        serverComms = new ServerComms();
        // Set up Calendar:
        monthTextView.setText(dateFormatForMonth.format(compactCalendarView.getFirstDayOfCurrentMonth()));

        String jsonString3 = serverComms.getFeature("historicRuns");

        System.out.println(jsonString3);
        List<String> runsArray1 = Arrays.asList(jsonString3.split("(?=\\{)|(?<=\\})"));
        ArrayList<String> runsArrayFinal = new ArrayList<String>();
        ArrayList<Historic_run> historic_runArrayList = new ArrayList<Historic_run>();


        for(String run : runsArray1) {
            if (run != null) {
                if (run.length() > 10) {
                    System.out.println(run);
                    runsArrayFinal.add(run);
                    //runsArrayFinal.add(run);
                    // runsArray1.remove(run);
                    //System.out.println(run);
                    Historic_run historic_run = gson.fromJson(run, Historic_run.class);
//                    System.out.println(historic_run);
                    historic_runArrayList.add(historic_run);
                }
            }
        }





        //String[] runsArray = jsonString3.split("(?=\\})");





//        JSONObject req = new JSONObject(join(LoadStrings(jsonString)));
//        Object obj = parser.parse(jsonString);
//        JSONArray array = (JSONArray)obj;
//        System.out.println(array);
//        System.out.println(array.get(1));

//        System.out.println(runsArray);

//        for(String run : runsArray){
////            System.out.println(run);
//            JsonReader reader = new JsonReader(new StringReader(run));
//            reader.setLenient(true);
//
//            Historic_run historic_run = gson.fromJson(run ,Historic_run.class);
//
//            System.out.println(historic_run.Datetime_Start);
//            historic_runArrayList.add(historic_run);
//        }



        BarChart barChart = (BarChart) view.findViewById(R.id.Bar_chart);
        ArrayList<BarEntry> yValues = new ArrayList<>();

        formatter = new SimpleDateFormat("d/M/y H:m");

        for(Historic_run run : historic_runArrayList){
            System.out.println(run.DateTime_Start);

            String str_date = run.DateTime_Start;
            Date date = new Date();
            try {
                date = (Date) formatter.parse(str_date);

            } catch (java.text.ParseException e) {
                e.printStackTrace();
            }
            long unixTime = (long) date.getTime()/1000;
            System.out.println(unixTime);
            float steps = Float.parseFloat(run.Number_Of_Steps);
            float UP = Float.parseFloat(run.Count_UP);
            float NP = Float.parseFloat(run.Count_NP);
            float OP = Float.parseFloat(run.Count_OP);

            yValues.add(new BarEntry( unixTime/1000,new float[]{UP,NP,OP}));
            Event event = new Event(0xFF000000, unixTime , "Run" );

            compactCalendarView.addEvent(event,true);
        }






        BarDataSet dataSet = new BarDataSet(yValues,"");
        dataSet.setDrawIcons(false);
        ArrayList<String> colors = new ArrayList<>();
        colors.add("#ffe95451");
        dataSet.setColors(new int[] {-60179113,-00255, -255105970});

        dataSet.setStackLabels(new String[]{"Over", "Under", "Normal"});
        BarData barData = new BarData(dataSet);
        barChart.setData(barData);
//        String[] labels = { "1","2","3","4","5"};
//        barChart.getXAxis().setValueFormatter(new IndexAxisValueFormatter(labels));
        final XAxis xAxis = barChart.getXAxis();
        xAxis.setPosition(XAxis.XAxisPosition.BOTTOM);
        xAxis.setTextSize(10f);
        xAxis.setTextColor(Color.RED);
        xAxis.setDrawAxisLine(true);
        xAxis.setDrawGridLines(true);
        Legend legend = barChart.getLegend();
        legend.setPosition(Legend.LegendPosition.ABOVE_CHART_CENTER);
        barChart.invalidate();

        // Calendar Listeners
        compactCalendarView.setListener(new CompactCalendarView.CompactCalendarViewListener() {
            @Override
            public void onDayClick(Date dateClicked) {
                System.out.println(dateClicked);
                List<Event> events = compactCalendarView.getEvents(dateClicked);
                System.out.println(events);
//                xAxis.setAxisMaximum(float 100);
//                graph.getViewport().setMinX(1);
//                graph.getViewport().setMaxX(3);
//                graph.addSeries(series);
            }

            @Override
            public void onMonthScroll(Date firstDayOfNewMonth) {
                System.out.println("month scrolled");
                //  System.out.println(dateFormatForMonth.format(compactCalendarView.getFirstDayOfCurrentMonth()));
                monthTextView.setText(dateFormatForMonth.format(compactCalendarView.getFirstDayOfCurrentMonth()));
            }

        });



        return view;
    }

    private class Historic_run {
        public String DateTime_Start;
        public String DateTime_End;
        public String Number_Of_Steps;
        public String Count_NP;
        public String Count_OP;
        public String Count_UP;
        public String averageFrequency;

        public Historic_run(String DateTime_Start,String DateTime_End,String Number_Of_Steps,String Count_NP,String Count_OP, String Count_UP,String averageFrequency){
            this.DateTime_Start = DateTime_Start;
            this.DateTime_End = DateTime_End;
            this.Number_Of_Steps = Number_Of_Steps;
            this.Count_NP = Count_NP;
            this.Count_OP = Count_OP;
            this.Count_UP = Count_UP;
            this.averageFrequency = averageFrequency;
        }
    }

}

