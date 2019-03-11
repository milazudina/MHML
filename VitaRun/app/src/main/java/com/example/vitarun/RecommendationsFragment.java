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

    private FragmentAlistener listener;
    private TextView editText;
    private Button buttonOk;

    public interface FragmentAlistener {
        void onInputASent(CharSequence input);
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_recommendations, container, false);

        editText = v.findViewById(R.id.firstrecom_body);
        buttonOk = v.findViewById(R.id.button_ok);
        buttonOk.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                CharSequence input = "Overpronation";
                listener.onInputASent(input);

            }

        });

        return v;
    }

    public void updateEditText(CharSequence newText) {
        editText.setText(newText);
    }


//    @Override
//    public void onAttach(Context context) {
//        super.onAttach(context);
//        if (context instanceof FragmentAlistener) {
//            listener = (FragmentAlistener) context;
//        } else {
//            throw new RuntimeException(context.toString()
//                    + "must implement FragmentAlistener");
//        }
//    }
//
//    @Override
//    public void onDetach() {
//        super.onDetach();
//        listener = null;
//    }


}

