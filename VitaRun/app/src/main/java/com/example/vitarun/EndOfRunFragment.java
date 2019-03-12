package com.example.vitarun;

import android.content.Context;
import android.net.Uri;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ViewSwitcher;


public class EndOfRunFragment extends Fragment {

    public ViewSwitcher mViewSwitcher;
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_end_of_run, container, false);
        mViewSwitcher = (ViewSwitcher) view.findViewById(R.id.viewSwitcher);
        mViewSwitcher.reset();
        return view;
    }
}