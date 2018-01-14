var userChoice = prompt("Do you choose rock, paper, scissors, lizard, or Spock?");
if (userChoice != "rock" || userChoice != "paper" || userChoice != "scissors" || userChoice != "lizard" || userChoice != "Spock") {
	console.log("Please choose either rock, paper, scissors, lizard, or Spock.");
}
var computerChoice = Math.random();
if (computerChoice < 0.2) {
	computerChoice = "rock";
} else if (computerChoice >= 0.2 && computerChoice < 0.4) {
	computerChoice = "paper";
} else if (computerChoice >= 0.4 && computerChoice < 0.6) {
	computerChoice = "scissors";
} else if (computerChoice >= 0.6 && computerChoice < 0.8) {
	computerChoice = "lizard";
} else {
	computerChoice = "Spock";
} console.log("Computer: " + computerChoice);
var compare = function (choice1, choice2) {
	if (choice1 === choice2) {
		return "The result is a tie!";
	} else if (choice1 == "rock") {
		if (choice2 == "scissors") {
			return "rock crushes scissors";
		} else if (choice2 == "paper") {
			return "paper covers rock";
		} else if (choice2 == "lizard") {
			return "rock crushes lizard";
		} else {
			return "Spock vaporizes rock";
		}
	} else if (choice1 == "paper") {
		if (choice2 == "rock") {
			return "paper covers rock";
		} else if (choice2 == "scissors") {
			return "scissors cuts paper";
		} else if (choice2 == "lizard") {
			return "lizard eats paper";
		} else {
			return "paper disproves Spock";
		}
	} else if (choice1 == "scissors") {
		if (choice2 == "rock") {
			return "rock crushes scissors";
		} else if (choice2 == "paper") {
			return "scissors cuts paper";
		} else if (choice2 == "lizard") {
			return "scissors decapitates lizard";
		} else {
			return "Spock smashes scissors";
		}
	} else if (choice1 == "lizard") {
		if (choice2 == "rock") {
			return "rock crushes lizard";
		} else if (choice2 == "paper") {
			return "lizard eats paper";
		} else if (choice2 == "scissors") {
			return "scissors decapitates lizard";
		} else {
			return "lizard poisons Spock"
		}
	} else if (choice1 == "Spock") {
		if (choice2 == "rock") {
			return "Spock vaporizes rock";
		} else if (choice2 == "paper") {
			return "paper disproves Spock";
		} else if (choice2 == "scissors") {
			return "Spock smashes scissors";
		} else {
			return "lizard poisons Spock";
		}
		}
}
compare (userChoice, computerChoice);