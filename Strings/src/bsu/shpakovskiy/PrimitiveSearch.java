package bsu.shpakovskiy;

public class PrimitiveSearch {
    public static void search(String sample, String txt)
    {
        System.out.println("i  j  i+j  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24");
        System.out.println("------------------------------------------------------------------------------------");
        System.out.print("     text->");
        int M=sample.length();
        int N=txt.length();
        int flag=0;
        StringBuilder blank= new StringBuilder("");

        System.out.println(txt.replace("", "  ").trim());

        for(int i=0;i<=N-M;i++)
        {
            int j;
            int s;
            for(j=0;j<M;j++)
            {
                s=i+j;

                if(txt.charAt(i+j)!=sample.charAt(j))
                    break;
                blank= new StringBuilder("");
                for (int l=0; l<i;l++) {
                    blank.append("   ");
                }
                System.out.println(i+"  "+j+"   " + s + "   "+blank+sample.replace("", "  ").trim());
            }
            if(j==M) {
                System.out.println("Подстрока найдена, вхождение с элемента под номером "+ i);
                flag=1;
                }
        }
        if(flag==0)
        { System.out.println("Подстрока не найдена");}
    }
}
