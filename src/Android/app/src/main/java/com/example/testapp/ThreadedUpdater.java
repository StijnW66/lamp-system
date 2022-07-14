package com.example.testapp;

import android.app.Activity;
import android.view.View;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;


public class ThreadedUpdater extends Thread{

    View main_view;
    Activity activity;

    public ThreadedUpdater(View main_view, Activity activity) {
        this.main_view = main_view;
        this.activity = activity;
    }

    public void run() {

        while (true) {
            JSONObject json = ServerConnection.get_rgb_values_update_http(1);

            if (json != null) {
                try {
                    int pattern = json.getInt("patternId");

                    updateView("Current Pattern: " + pattern);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private void updateView(String text) {
        activity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                TextView textView = main_view.findViewById(R.id.textview_pattern);
                textView.setText(text);
            }
        });
    }
}
