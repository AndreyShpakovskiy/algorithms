package bsu.shpakovskiy;

import java.util.ArrayList;
import java.util.Collections;

public class MultipleRepetitionSearch {
    public static int searchrepetitions(String sample, String txt){
        int M=sample.length();
        int N=txt.length();
        int flag=0;
        int k=1;
        ArrayList<Integer> ans = new ArrayList<Integer>();
        ArrayList<Integer> ans1 = new ArrayList<Integer>();
        ArrayList<Integer> ans2 = new ArrayList<Integer>();
        for(int i=0;i<=N-M;i++)
        {
            int j;
            for(j=0;j<M;j++)
            {
                if(txt.charAt(i+j)!=sample.charAt(j))
                    break;
            }
            if(j==M) {
                flag=1;
                ans.add(i);
            }
        }
        if(flag!=0)
        { for (int i=1;i<ans.size();i++) {
            if(ans.get(i)-ans.get(i-1)==M)
            {
                k+=1;
            }
            else
            {
                ans1.add(k);
                ans2.add(ans.get(i-1)-M*(k-1));
                k=1;
            }

        }
            ans1.add(k);
            ans2.add(ans.get(ans.size()-1)-M*(k-1));
            for (int i=0;i<ans1.size();i++)
            {
                if(Collections.max(ans1).equals(ans1.get(i)))
                {
                    return ans2.get(i);
                }
            }
            }



       return 0;
    }
    }
