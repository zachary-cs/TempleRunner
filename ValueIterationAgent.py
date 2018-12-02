from GameEngine import *


class ValueIterationAgent:

    def __init__(self, engine, discount=0.5, iterations=100):

        # Keep a reference to the GameEngine
        self.engine = engine
        # Set our Value Iteration vars
        self.values = {}
        self.discount = discount
        self.iterations = iterations

        # Value Iteration Code BEGINS HERE

        # Make sure the engine passed in is the GameEngine
        if isinstance(engine, GameEngine):
            # Get all States
            gameStates = self.engine.GetAllStates()

            # Loop through interations
            for i in range(0, self.iterations):
                # Create a copy of previous state values
                values_prime = self.values.copy()
                #Loop through all states
                for state in gameStates:
                    prime_values = []
                    # Place the player at this state to test their actions
                    engine.PlacePlayer(state.GetCoords())
                    # print("Testing at state:" + str(state))
                    for direction, cadence in engine.GetAllPossibleActions():
                        # print("Direction: " + direction + " | Cadence: " + cadence)
                        val_prime = 0
                        statePrime, probability = engine.GetTransitionStateAndProb(direction, cadence)
                        # Obtain the sum of Reward(s) + Discount * (P(s'| s,a)*R(s'))
                        reward = engine.GetReward()
                        if statePrime in values_prime.keys():
                            val_prime = probability * (reward + (self.discount * values_prime[statePrime]))
                        else:
                            val_prime = probability * reward
                        prime_values.append(val_prime)
                    self.values[state] = max(prime_values)

            for key in self.values.keys():
                print("Key: " + str(key) + " | Value: " + self.values[key])






        else:
            print(" Please use the GameEngine as the first argument")
            return







        # End Value iteration code
        return

    # Incoming State should be the tile coordinates
    # Ex. state = (4,6)
    def getValue(self, state):
        return self.values[state]
