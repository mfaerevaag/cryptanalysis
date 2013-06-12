package week1;

public class SubstitutionCipher {

	private static int[] plaintext = new int[] { 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
			3, 3, 3, 3, 3, 3 };
	private static int[] key = new int[] { 13, 4, 3, 12, 1, 0, 8, 10, 14, 6, 9,
			15, 11, 2, 5, 7 };
	private static int[] cipher = new int[16];
	private static int initVector;

	public static void main(String[] args) {

		vectorInit();

	}

	private static void vectorInit() {
		for (int i = 0; i < plaintext.length; i++) {

			initVector = i;
			encrypt(plaintext, initVector);

			System.out.print("Init vector: " + initVector + " Cipher: ");
			for (int j = 0; j < cipher.length; j++) {
				System.out.print(cipher[j] + " ");

			}
			System.out.println("");
		}
	}

	private static void encrypt(int[] plaintext, int initVector) {

		cipher[0] = key[(plaintext[0] ^ initVector)];

		for (int i = 1; i < 16; i++) {
			cipher[i] = key[cipher[i - 1] ^ plaintext[i]];
		}

	}

}