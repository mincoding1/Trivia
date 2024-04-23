import java.util.Random;

public class GameRunner {
    public static void main(String[] args) {
        boolean notAWinner;

        Game aGame = new Game();

        aGame.add("Chet");
        aGame.add("Pat");
        aGame.add("Sue");

        Random rand = new Random();

        do {
            aGame.rolling();

            if (rand.nextInt(9) == 7) {
                notAWinner = aGame.wrongAnswer();
            } else {
                notAWinner = aGame.wasCorrectlyAnswered();
            }
        } while (notAWinner);
    }
}
