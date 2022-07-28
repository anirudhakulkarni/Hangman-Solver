/* boilerplate code*/
import java.util.Scanner;
import java.util.ArrayList;
import java.math.BigInteger;
public class test {
    public static void main(String[] args) {
        String md5hash="386b8fe06ad1d01e027de7270f48822";
        // const hex="0x386b8fe06ad1d01e027de7270f48822";
        // System.out.println(digest);
        // BigInteger bi = new BigInteger(digest, 16);
        // byte byteArray[] = bigInteger.toByteArray();
        byte byteArray[] = md5hash.getBytes();
        String digest = String.format("%032x", new BigInteger(1, byteArray));
        // String.format("%032x", new BigInteger(1, m.digest()));
        System.out.println(digest);
    }
}
 
// 5ca67533ee5690e21b5786c6b8e5422e
// 386b8fe06ad1d01e027de7270f48822