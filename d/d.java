import java.util.Hashtable;
import java.util.Scanner;

public class d {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        // String a = "erf";
        // String b = "wh wa wa";
        Boolean result = true;
        Hashtable<Character, String> h = new Hashtable<Character, String>();
        Hashtable<String, String> h2 = new Hashtable<String, String>();
        String[] w = b.split(" ");
        if (w.length == a.length()) {
            for (int i = 0; i < a.length(); i++) {
                String string = h.get(a.charAt(i));
                if (string == null) {
                    h.put(a.charAt(i), w[i]);
                    // System.out.println("Add: "+ a.charAt(i)+" " + w[i]);
                } else {
                    if (!string.equals(w[i])) {
                        result = false;
                        break;
                    }
                }
                ;
            }
            // System.out.println(result);
            for (int i = 0; i < a.length(); i++) {
                String token = h2.get(w[i]);
                if (token == null) {
                    h2.put(w[i], String.valueOf(a.charAt(i)));
                    // System.out.println("Add: "+ w[i]+" " + String.valueOf(a.charAt(i)));
                } else {
                    if (!token.equals(String.valueOf(a.charAt(i)))) {
                        // System.out.println("Error: "+ token+" " +String.valueOf(a.charAt(i)));
                        result = false;
                        break;
                    }
                }
                ;
            }
            if (result) {
                System.out.println("True");
            } else {
                System.out.println("False");
            }
        } else {
            System.out.println("False");
        }
    }
}
