package com.example.vitarun;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

public class RunFragment extends Fragment {

    RunFragmentListener callback;


    public void setRunFragmentListener(Activity activity)
    {
        callback = (MainActivity) activity;
    }

    // Interface for controlling RunEvent in MainActivity.
    public interface RunFragmentListener {
        void StartRun();
        void PauseRun();
        void EndRun();
    }

    public RecommendationsFragment recommendationsFragment;
    public EndOfRunFragment endOfRunFragment;


    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        recommendationsFragment = new RecommendationsFragment();
        endOfRunFragment = new EndOfRunFragment();
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {

        getChildFragmentManager().beginTransaction().replace(R.id.run_recommendation_container,
                recommendationsFragment).commit();
        getChildFragmentManager().beginTransaction().replace(R.id.run_transportControl_container,
                new TransportControlFragment()).commit();
        getChildFragmentManager().beginTransaction().replace(R.id.run_title_container,
                new RunTitleFragment()).commit();
        getChildFragmentManager().beginTransaction().replace(R.id.end_of_run_container,
                endOfRunFragment).commit();


        return inflater.inflate(R.layout.fragment_run, container, false);

    }

}

