package com.example.vitarun;


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


/**
 * A simple {@link Fragment} subclass.
 */
public class TransportControlFragment extends Fragment {
    ViewSwitcher mViewSwitcher;
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_transport_control, container, false);
        mViewSwitcher = view.findViewById(R.id.profileSwitcher);
        Button button = (Button) view.findViewById(R.id.start_run_button);
        Button stopButton = (Button) view.findViewById(R.id.stop_button);
        Button pauseButton = (Button) view.findViewById(R.id.pause_button);

        button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v ) {
                System.out.println("change view"); // some function here
                // mViewSwitcher.setDisplayedChild(0);
                mViewSwitcher.showNext();
                System.out.println("change view complete?");

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

    };

}

