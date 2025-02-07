import json


class NFATransition:
    """
    Represents a transition in a non-deterministic finite automaton (NFA).
    """

    def __init__(self, label: str, destination: 'NFAState'):
        """
        Initializes a new transition.
        :param label: The transition symbol (or 'ε' for epsilon transitions).
        :param destination: The state to which this transition goes.
        """
        self.label = label
        self.destination = destination


class NFAState:
    """
    Represents the state of a non-deterministic finite automaton (NFA).
    """

    def __init__(self, label: str):
        """
        Initializes a new state.
        :param label: The label of the state.
        """
        self.label = label
        self.transitions = []  # List of NFATransition objects

    def add_transition(self, label: str, destination: 'NFAState'):
        """
        Adds a transition to the state.
        :param label: The label for the transition (character or epsilon).
        :param destination: The destination state.
        """
        self.transitions.append(NFATransition(label, destination))

    def epsilon_closure(self, visited=None) -> set:
        """
        Computes the epsilon closure of this state.
        :param visited: A set of visited states to avoid infinite loops.
        :return: A set containing this state and all states reachable via epsilon transitions.
        """
        if visited is None:
            visited = set()

        if self in visited:
            return set()

        visited.add(self)
        closure = {self}

        for transition in self.transitions:
            if transition.label == 'ε':  # Epsilon transition
                closure |= transition.destination.epsilon_closure(visited)

        return closure

    def get_transitions(self, label: str) -> set:
        """
        Returns the set of states reachable from this state via a given label.
        :param label: The label for the transition.
        :return: A set of destination states.
        """
        return {t.destination for t in self.transitions if t.label == label}


def simulate_nfa(start_state: NFAState, accepting_states: set[NFAState], input_string: str) -> bool:
    """
    Simulates an NFA on a given input string.
    :param start_state: The initial state of the NFA.
    :param input_string: The input string to process.
    :param accepting_states: The set of accepting states.
    :return: True if the NFA accepts the input string, False otherwise.
    """
    current_states = start_state.epsilon_closure()

    for symbol in input_string:
        next_states = set()
        for state in current_states:
            next_states |= state.get_transitions(symbol)

        current_states = set()
        for state in next_states:
            current_states |= state.epsilon_closure()

    return any(state in accepting_states for state in current_states)


def load_nfa_from_json(json_file: str):
    """
    Loads an NFA from a JSON file.
    :param json_file: Path to the JSON file.
    :return: The initial state and set of accepting states.
    """
    with open(json_file, 'r') as file:
        data = json.load(file)

    states = {state_data["label"]: NFAState(state_data["label"]) for state_data in data["states"]}

    for state_data in data["states"]:
        state = states[state_data["label"]]
        for transition in state_data["transitions"]:
            state.add_transition(transition["label"], states[transition["to_state"]])

    initial_state = states[data["initial_state"]]
    accepting_states = {states[label] for label in data["accepting_states"]}

    return initial_state, accepting_states
