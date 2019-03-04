package com.example.vitarun;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;

public class RunEvent {

    Date startTime;
    Date endTime;

    ArrayList<float> DATA_BUFFER;

    public RunEvent()
    {
        this.startTime = Calendar.getInstance().getTime();

        DATA_BUFFER = new ArrayList<>();
    }

    public void PauseRun()
    {

    }

    public void EndRunEvent()
    {
        endTime = Calendar.getInstance().getTime();
    }



}
