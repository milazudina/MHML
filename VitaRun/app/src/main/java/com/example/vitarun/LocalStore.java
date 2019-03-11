package com.example.vitarun;

import android.content.Context;
import android.content.SharedPreferences;

public class LocalStore {
    public static final String SP_NAME = "userDetails";
    SharedPreferences useLocalDatabase;


    public LocalStore(Context context){
        useLocalDatabase = context.getSharedPreferences(SP_NAME, 0);

    }
    public void storeUserData(User user) {
        SharedPreferences.Editor spEditor = useLocalDatabase.edit();
        spEditor.putString("username", user.username);
        spEditor.putInt("age", user.age);
        spEditor.putString("name", user.name);

        spEditor.putString("password", user.password);
        spEditor.putInt("weight", user.weight);
        spEditor.commit();

    }

    public User getLoggedInUser(){
        String username = useLocalDatabase.getString("username", "");
        String name = useLocalDatabase.getString("name", "");
        String password = useLocalDatabase.getString("password", "");

        int age = useLocalDatabase.getInt("age", -1);
        int weight = useLocalDatabase.getInt("weight", -1);

        User storedUser = new User(username, password, name, age, weight);

        return  storedUser;
    }

    public void setUserLoggedIn(Boolean loggedIn){
        SharedPreferences.Editor spEditor = useLocalDatabase.edit();
        spEditor.putBoolean("loggedIn", loggedIn);
        spEditor.commit();
    }

    public boolean getUserLoggedIn(){
        return useLocalDatabase.getBoolean("loggedIn", false);

    }
    public void clearUserData(){
        SharedPreferences.Editor spEditor = useLocalDatabase.edit();
        spEditor.clear();
        spEditor.commit();
    }
}
