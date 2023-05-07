import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;

public class BOJ2470 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		ArrayList<Integer> inputs = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(st.nextToken());
			inputs.add(num);
		}
		Collections.sort(inputs);

		int start = 0;
		int end = N - 1;
		int min = 2000000000;
		int resStart = 0, resEnd = 0;

		while (start < end) {
			int sum = Math.abs(inputs.get(start) + inputs.get(end));
			if (sum < min) {
				min = sum;
				resStart = start;
				resEnd = end;
			}

			int caseOne = Math.abs(inputs.get(start) + inputs.get(end - 1));
			int caseTwo = Math.abs(inputs.get(start + 1) + inputs.get(end));
			if (caseOne < caseTwo) {
				end--;
			} else {
				start++;
			}
//			System.out.println(start + " " + end + " " + sum);
		}
//		System.out.println(inputs);
//		System.out.println(resStart + " " + resEnd);
		sb.append(inputs.get(resStart)).append(" ").append(inputs.get(resEnd)).append("\n");
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}
}

