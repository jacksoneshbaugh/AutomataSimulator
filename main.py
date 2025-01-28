import json
from automata import DFATransition, DFAState, DeterministicFiniteAutomaton


def parse_dfa_from_json(file_name: str) -> DeterministicFiniteAutomaton:
    """
    Parses a JSON string to create a DeterministicFiniteAutomaton object.
    :param file_name: Path to the JSON file describing the DFA.
    :return: An instance of DeterministicFiniteAutomaton.
    """
    with open(file_name, 'r') as json_file:
        # Load JSON data
        data = json.load(json_file)

        # Parse the alphabet
        alphabet = data["alphabet"]

        # Create a dictionary of states by their labels
        states_dict = {state["label"]: DFAState(state["label"], []) for state in data["states"]}

        # Add transitions to each state
        for state_data in data["states"]:
            state = states_dict[state_data["label"]]
            for transition_data in state_data["transitions"]:
                transition_label = transition_data["label"]
                to_state_label = transition_data["to_state"]
                to_state = states_dict[to_state_label]
                state.transitions.append(DFATransition(transition_label, to_state))

        # Get the initial state and accepting states
        initial_state = states_dict[data["initial_state"]]
        accepting_states = [states_dict[label] for label in data["accepting_states"]]

        # Get intermediate states (all states except initial and accepting)
        intermediate_states = [
            state for label, state in states_dict.items()
            if state is not initial_state and state not in accepting_states
        ]

        # Return the DFA
        return DeterministicFiniteAutomaton(alphabet, initial_state, intermediate_states, accepting_states)


if __name__ == "__main__":
    input_file = input("Please enter the path to the JSON file: ")
    dfa = parse_dfa_from_json(input_file)
    while True:
        test_string = input("Please enter the test string: ")
        if dfa.run(test_string):
            print('String accepted.')
        else:
            print('String rejected.')
        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break
    print('Goodbye!')
