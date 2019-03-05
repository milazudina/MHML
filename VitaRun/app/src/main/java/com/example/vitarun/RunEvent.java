package com.example.vitarun;

import java.time.Duration;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;

public class RunEvent {

    private ZonedDateTime startTime;
    private ZonedDateTime endTime;

    ArrayList<Float> DATA_BUFFER;

    public RunEvent()
    {
        this.startTime = ZonedDateTime.now(ZoneId.systemDefault());

        DATA_BUFFER = new ArrayList<>();
    }

    public void PauseRunEvent()
    {

    }

    public void EndRunEvent()
    {
        endTime = ZonedDateTime.now(ZoneId.systemDefault());

    }

    public Duration getEllapsedTime()
    {
        return Duration.between(startTime, ZonedDateTime.now(ZoneId.systemDefault()));
    }

    public ZonedDateTime getStartTime()
    {
        return startTime;
    }




}
