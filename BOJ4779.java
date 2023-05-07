import java.io.*;
import java.util.*;
import java.lang.*;
import java.math.*;

public class BOJ4779 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {

		String input = "";
		ArrayList<String> resArr = new ArrayList<>();
		resArr.add("-");
		resArr.add("- -");
		for (int i = 2; i <= 12; i++) {
			StringBuilder resSB = new StringBuilder();
			String tmpSB = " ".repeat(resArr.get(i - 1).length());
			resSB.append(resArr.get(i - 1)).append(tmpSB).append(resArr.get(i - 1));
			resArr.add(resSB.toString());
		}
		while ((input = br.readLine()) != null) {
			int num = Integer.parseInt(input);
			sb.append(resArr.get(num)).append("\n");
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}
}
