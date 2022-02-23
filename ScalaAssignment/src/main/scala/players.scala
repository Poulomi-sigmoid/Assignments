class players(var year: Int, var playerName: String, var country: String, var matches: Int, var runs: Int, var wickets: Int) {}

object players {

  def push_into(year: Int, playerName: String, country: String, matches: Int, runs: Int, wickets: Int): players = {
    var player = new players(year, playerName, country, matches, runs, wickets);
    return player;
  }

  def main(args: Array[String]): Unit = {
    val bufferedSource = scala.io.Source.fromFile("/Users/poulomichandra/Documents/players.csv")
    var players = List(push_into(2018, "Sumit", "India", 23, 675, 11))

    for (player <- bufferedSource.getLines){
      val columns = player.split(",").map(_.trim)
      players = players :+ push_into(columns(0).toInt, columns(1), columns(2), columns(3).toInt, columns(4).toInt, columns(5).toInt)
    }

    println("\nQ1. Player with the best highest runs scored.");
    var playerWithHighestRuns = players.sortBy(el => el.runs).reverse
    println(playerWithHighestRuns(0).playerName + " : " + playerWithHighestRuns(0).runs)
    println("\n======================================")
    println("\nQ2. Top 5 players by runs scored.")
    for (player <- playerWithHighestRuns.take(5)){
      println(player.playerName + " : " + player.runs)
    }

    println("\n======================================")
    println("\nQ3. Top 5 players by wicket taken.")
    var playerWithHighestWicket = players.sortBy(el => el.wickets).reverse
    for (player <- playerWithHighestWicket.take(5)) {
      println(player.playerName + " : " + player.wickets)
    }

    println("\n======================================")
    println("\nQ4. Rank players with overall performance give weight 5x to wicket taken and (5/100)x to run scored.")
    players = players.sortBy(el => el.wickets * 5).sortBy(el => el.runs * 0.05).reverse
    for (player <- players) {
      println(player.playerName)
    }
  }
}
