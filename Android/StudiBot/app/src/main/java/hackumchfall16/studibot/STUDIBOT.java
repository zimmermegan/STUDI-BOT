package hackumchfall16.studibot;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class STUDIBOT extends AppCompatActivity {
    DerpProxy proxy = new DerpProxy("73.173.48.240");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_studibot);

        //when you need to send a command, use this method
        int command=0;
        proxy.sendInfo(0);
    }



    private void sendCommand(int a){
        new AsyncTask(){

            @Override
            protected Object doInBackground(Object[] params) {
                proxy.sendInfo((Integer) params[0]);
                return null;
            }
        }.execute(new Integer(a));
    }
}
