package com.example.vitarun;


import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ViewSwitcher;


public class TransportControlFragment extends Fragment {
    ViewSwitcher mViewSwitcher;

    private RunFragment runFragment;

    RunTransportListener callback;

    public void setRunTransportListener(MainActivity activity)
    {
        callback = activity;
    }

    // Interface for controlling RunEvent in MainActivity.
    public interface RunTransportListener {
        void StartRun();
        void PauseRun();
        void EndRun();
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);

        // Get Reference to parent RunFragment.
        runFragment = (RunFragment)this.getParentFragment();
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_transport_control, container, false);
        mViewSwitcher = view.findViewById(R.id.profileSwitcher);
        Button startButton = (Button) view.findViewById(R.id.start_run_button);
        Button stopButton = (Button) view.findViewById(R.id.stop_button);
        Button pauseButton = (Button) view.findViewById(R.id.pause_button);

        startButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v ) {
//                System.out.println("change view"); // some function here
                // mViewSwitcher.setDisplayedChild(0);
                callback.StartRun();

                mViewSwitcher.showNext();
//                System.out.println("change view complete?");

            }
        });

        pauseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String text_pronate = "Pause";
                Intent speechIntent = new Intent(getActivity(), TextToSpeechService.class);

                callback.PauseRun();
                speechIntent.putExtra(TextToSpeechService.EXTRA_WORD, text_pronate );

                getActivity().startService(speechIntent);
            }
        });

        stopButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                System.out.println("change view"); // some function here
                // mViewSwitcher.setDisplayedChild(0);

                callback.EndRun();

                mViewSwitcher.showNext();
                System.out.println("change view complete?");
            }
        });
        return view;
    }

}

