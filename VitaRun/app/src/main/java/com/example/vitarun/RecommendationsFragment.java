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


/**
 * A simple {@link Fragment} subclass.
 */
public class RecommendationsFragment extends Fragment {



    CharSequence input = "Overpronation";

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
       View RootView = inflater.inflate(R.layout.fragment_recommendations, container, false);


        TextView tv = (TextView)RootView.findViewById(R.id.firstrecom_body);
        tv.setText(input);

//
        return RootView;
    }






}

