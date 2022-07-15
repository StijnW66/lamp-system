package com.example.testapp;

import android.os.Bundle;
import android.os.StrictMode;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;

import org.json.JSONException;
import org.json.JSONObject;


public class SecondFragment extends Fragment {

    long pattern = 0;


    @Override
    public View onCreateView(
            LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_second, container, false);
    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();

        StrictMode.setThreadPolicy(policy);

        View main_view = view;
        JSONObject json = ServerConnection.get_rgb_values_http(1);

        try {
            pattern = json.getInt("patternId");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        updateTextView(view, pattern);

        ThreadedUpdater updater = new ThreadedUpdater(main_view, getActivity());

//        view.findViewById(R.id.button_second).setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                NavHostFragment.findNavController(SecondFragment.this)
//                        .navigate(R.id.action_SecondFragment_to_FirstFragment);
//            }
//        });

        view.findViewById(R.id.increase_pattern).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                JSONObject json = ServerConnection.update_rgb_values_http(1, 1);

                try {
                    pattern = json.getLong("patternId");
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                updateTextView(main_view, pattern);
            }

        });

        view.findViewById(R.id.decrease_pattern).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                JSONObject json = ServerConnection.update_rgb_values_http(1, -1);

                try {
                    pattern = json.getLong("patternId");
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                updateTextView(main_view, pattern);
            }
        });

        updater.start();

    }



    public void updateTextView(View view, long pattern) {
        TextView textView = view.findViewById(R.id.textview_pattern);
        textView.setText("Current Pattern: " + pattern);
    }
}
