package com.example.testapp;




import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;

public class ServerConnection {

    private static String lastUpdated;
    private static long pattern;
    private static final int[] rgb =  {0, 0, 0};
    private static final String host = "https://cryptic-earth-79580.herokuapp.com";
    private static boolean updatedFlag = false;

    public static JSONObject get_rgb_values_http(long rgbId) {
        String path = "/rgb_values/" + rgbId;

        JSONObject json = null;
        try {
            URL url = new URL(host + path);

            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");

            BufferedReader in = new BufferedReader(
                    new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer content = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }

            json = new JSONObject(content.toString());

            in.close();
            con.disconnect();

            pattern = json.getInt("patternId");
            lastUpdated = json.getString("lastUpdated");

        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }


        return json;
    }

    public static JSONObject get_rgb_values_update_http(long rgbId) {
        String path = "/rgb_values/update/" + rgbId;

        JSONObject json = null;
        try {
            URL url = new URL(host + path);

            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestProperty("Date", lastUpdated);
            con.setRequestMethod("GET");


            System.out.println(con.getResponseCode());
            if (updatedFlag) {
                updatedFlag = false;
                return null;
            }

            BufferedReader in = new BufferedReader(
                    new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer content = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }

            if (content.length() == 0) {
                return null;
            }

            json = new JSONObject(content.toString());

            in.close();
            con.disconnect();

            pattern = json.getInt("patternId");
            lastUpdated = json.getString("lastUpdated");

        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }

        return json;
    }

    public static JSONObject update_rgb_values_http(long rgbId, int change) {
        updatedFlag = false;
        String path = "/rgb_values/" + rgbId;

        JSONObject json = null;
        try {
            URL url = new URL(host + path);

            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("PATCH");

            con.setRequestProperty("Content-Type", "application/json; utf-8");
            con.setRequestProperty("Accept", "application/json");
            con.setDoOutput(true);


            String jsonInput = "{\"rgb\": " + Arrays.toString(rgb) + " ,\"patternId\":" + (pattern + change) + "}";

            try(OutputStream os = con.getOutputStream()) {
                byte[] input = jsonInput.getBytes("utf-8");
                os.write(input, 0, input.length);
            }


            BufferedReader in = new BufferedReader(
                    new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer content = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }

            json = new JSONObject(content.toString());

            in.close();
            con.disconnect();

            pattern = json.getInt("patternId");
            lastUpdated = json.getString("lastUpdated");

            updatedFlag = true;
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }

        return json;
    }
}
