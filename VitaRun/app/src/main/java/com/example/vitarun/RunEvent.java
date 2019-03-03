package com.example.vitarun;

import java.util.Calendar;
import java.util.Date;

public class RunEvent {

    Date startTime;
    Date endTime;


    public RunEvent()
    {
        startTime = Calendar.getInstance().getTime();

    }

    public void EndRun()
    {
        endTime = Calendar.getInstance().getTime();
    }

}
