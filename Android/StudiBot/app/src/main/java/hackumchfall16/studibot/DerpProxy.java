package hackumchfall16.studibot;
import android.os.AsyncTask;

import java.net.*;
import java.io.*;

/**
 * Created by Birdman on 10/1/2016.
 */

public class DerpProxy {
    private String ip;
    public DerpProxy(String ip){
        this.ip=ip;
    }

    public boolean sendInfo(int a){
        try {
                    Socket s = new Socket(ip,25570);
                    PrintWriter pw = new PrintWriter(s.getOutputStream());
                    pw.write(a);
                } catch (IOException e) {
                    e.printStackTrace();
                }


        return true;
    }
}
