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

    public void setRunTransportListener(Activity activity)
    {
        callback = activity;
    }

    public interface RunTransportListener {
        void StartRun();
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
                System.out.println("change view"); // some function here
                // mViewSwitcher.setDisplayedChild(0);
                mViewSwitcher.showNext();
                System.out.println("change view complete?");

                StartRun();

                // This Changes Fragments:
//                FragmentManager fm = getFragmentManager();
//                TransportControlFragment f = (TransportControlFragment) fm.findFragmentById(R.id.transport_control_fragment);
//                if (f == null) {
//                    getFragmentManager()
//                            .beginTransaction()
//                            .replace(R.id.run_transportControl_container, new TransportControlFragment())
//                            .commit();
//                }
            }
        });

        pauseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String text_pronate = "Pause";
                Intent speechIntent = new Intent(getActivity(), TextToSpeechService.class);

                speechIntent.putExtra(TextToSpeechService.EXTRA_WORD, text_pronate );

                getActivity().startService(speechIntent);
            }
        });

        stopButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                System.out.println("change view"); // some function here
                // mViewSwitcher.setDisplayedChild(0);
                mViewSwitcher.showNext();
                System.out.println("change view complete?");
            }
        });
        return view;
    }


    // Call Run Methods in Parent Run Fragment.
    private void StartRun()
    {
        runFragment.StartRun();
    }

    public void PauseRun()
    {
        runFragment.PauseRun();
    }

    public void StopRun()
    {
        runFragment.StopRun();
    }
}

