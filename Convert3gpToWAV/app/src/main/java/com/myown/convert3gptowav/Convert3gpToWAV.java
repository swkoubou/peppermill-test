package com.myown.convert3gptowav;

import android.content.Context;
import android.content.res.AssetManager;
import android.util.Log;

import com.github.hiteshsondhi88.libffmpeg.ExecuteBinaryResponseHandler;
import com.github.hiteshsondhi88.libffmpeg.FFmpeg;
import com.github.hiteshsondhi88.libffmpeg.LoadBinaryResponseHandler;
import com.github.hiteshsondhi88.libffmpeg.exceptions.FFmpegCommandAlreadyRunningException;
import com.github.hiteshsondhi88.libffmpeg.exceptions.FFmpegNotSupportedException;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintStream;

/**
 * Created by Yuta.Watanabe on 2016/07/23.
 */
public class Convert3gpToWAV {
	public void convert(Context context){
		AssetManager am = context.getAssets();
		InputStream is = null;
		try {
			is = am.open("audiorecordtest.3gp");
		}catch (IOException e){
			e.printStackTrace();
		}
		File file = createFileFromInputStream(is);

		String fpstr = file.getAbsolutePath();
		String outname = "/data/data/" + context.getPackageName() + "/audiorecordtest.wav";
		convert(fpstr, outname);
//		String exeQuery = "ffmpeg -i "+fpstr+" -acodec pcm_u8 "+outname;
//		try {
//			Runtime.getRuntime().exec(exeQuery);
//		}catch (IOException e){
//			e.printStackTrace();
//		}
	}

	public void convert(String fileabsolutepath, String outname){
		String exeQuery = "ffmpeg -i "+fileabsolutepath+" -acodec pcm_u8 "+outname;
		try {
			Runtime.getRuntime().exec(exeQuery);
		}catch (IOException e){
			e.printStackTrace();
		}
	}

	private File createFileFromInputStream(InputStream inputStream) {
		try{
			File f = new File("/data/data/com.myown.convert3gptowav/audiorecordtest.wav");
			OutputStream outputStream = new FileOutputStream(f);
			byte buffer[] = new byte[1024];
			int length = 0;

			while((length=inputStream.read(buffer)) > 0) {
				outputStream.write(buffer,0,length);
			}

			outputStream.close();
			inputStream.close();

			return f;
		}catch (IOException e) {
			//Logging exception
			e.printStackTrace();
		}

		return null;
	}
}
