package week1;

import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;

public class crypto {

	private static byte[] cipher;

	public static void main(String[] args) throws UnsupportedEncodingException,
			InvalidKeyException, NoSuchAlgorithmException,
			NoSuchPaddingException, IllegalBlockSizeException,
			BadPaddingException {

		String key = "hejmeddhaamaddas";
		String plaintext = "elephants IsNice";

		encrypt(key.getBytes(), plaintext.getBytes());
		decrypt(key.getBytes(), cipher);
		bruteforce(cipher, plaintext.getBytes());
	}

	private static byte[] encrypt(byte[] key, byte[] plaintext)
			throws NoSuchAlgorithmException, NoSuchPaddingException,
			InvalidKeyException, IllegalBlockSizeException, BadPaddingException {
		Cipher c = Cipher.getInstance("AES");
		SecretKeySpec k = new SecretKeySpec(key, "AES");
		c.init(Cipher.ENCRYPT_MODE, k);

		cipher = c.doFinal(plaintext);

		for (int i = 0; i < cipher.length; i++) {
			System.out.print(cipher[i]);
		}

		byte[] cip = cipher;
		return cip;

	}

	private static void decrypt(byte[] key, byte[] cipher)
			throws NoSuchAlgorithmException, NoSuchPaddingException,
			InvalidKeyException, IllegalBlockSizeException, BadPaddingException {

		Cipher c = Cipher.getInstance("AES");
		SecretKeySpec k = new SecretKeySpec(key, "AES");
		c.init(Cipher.DECRYPT_MODE, k);

		byte[] data = c.doFinal(cipher);
		System.out.println("");
		for (int i = 0; i < data.length; i++) {
			System.out.print((char) data[i]);
		}

	}

	private static void bruteforce(byte[] cipher, byte[] plaintext)
			throws InvalidKeyException, NoSuchAlgorithmException,
			NoSuchPaddingException, IllegalBlockSizeException,
			BadPaddingException {
		System.out.println("");
		byte[] key = "AAAAAAAAAAAAAAAA".getBytes();
		
		int count = 0;
		
		
	}
}	