package bsu.shpakovskiy;

public class Main {
    public static void main(String[] args)
    {
        String text1="AAAAAAAAAAAAAAAAAAAB";
        String sample1="AAAAAAAB";
        String text2="ABABABABAABABABABAAAAAAAA";
        String sample2="ABABABAB";

        PrimitiveSearch.search(sample1,text1);
        PrimitiveSearch.search(sample2,text2);

        String text3="CABABDABABABFWABDABQQE";
        String sample3="AB";
        System.out.println("Индекс начала самого длинного кратного повторения: "+MultipleRepetitionSearch.searchrepetitions(sample3,text3));
    }
}
