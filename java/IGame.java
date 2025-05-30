public interface IGame {
    public boolean add(String playerName);
    public void rolling(int roll);
    public boolean wasCorrectlyAnswered();
    public boolean wrongAnswer();
}
