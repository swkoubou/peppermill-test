package com.example.uryoya.record_test;

import android.content.Context;

import com.github.hiteshsondhi88.libffmpeg.FFmpeg;
import com.github.hiteshsondhi88.libffmpeg.LoadBinaryResponseHandler;
import com.github.hiteshsondhi88.libffmpeg.exceptions.FFmpegNotSupportedException;

import java.io.File;

/**
 * Created by Yuta.Watanabe on 2016/07/23.
 */
public class ConvertWAV {
	private String path = null;

	public ConvertWAV(String file_path){
		this.path = file_path;
	}

	public File convert(Context context){

		FFmpeg fFmpeg = FFmpeg.getInstance(context);
		try{
			fFmpeg.loadBinary(new LoadBinaryResponseHandler(){
				@Override
				public void onStart() {}

				@Override
				public void onFailure() {}

				@Override
				public void onSuccess() {}

				@Override
				public void onFinish() {}
			});
		}catch (FFmpegNotSupportedException e){
			e.printStackTrace();
		}

	}

}
