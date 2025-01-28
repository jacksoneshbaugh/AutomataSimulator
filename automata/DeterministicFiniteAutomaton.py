from automata import DFAState


class DeterministicFiniteAutomaton:
    """
    Represents a finite automaton.
    """
    def __init__(self, alphabet: list[chr], initial_state: DFAState, intermediate_states: list[DFAState], accepting_states: list[DFAState]):
        """
        Initializes a finite automaton.
        :param alphabet: the alphabet of the automaton
        :param initial_state: the initial state of the automaton
        :param intermediate_states: the intermediate states of the automaton
        :param accepting_states: the accepting states of the automaton
        """
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.intermediate_states = intermediate_states
        self.accepting_states = accepting_states

    def run(self, input_sequence: str) -> bool:
        """
        Given an input sequence, runs the automaton on the input sequence.
        :param input_sequence: the input sequence to run the automaton on
        :return: True if the final state of the automaton is the accepting state, False otherwise
        """
        current_state = self.initial_state

        for char in input_sequence:
            if char not in self.alphabet:
                raise ValueError(f'Character `{char}` not in alphabet: {self.alphabet}')

            current_state = current_state.transition(char).state
            if current_state is None:
                raise ValueError(f'Missing transition! Automata must have paths for all alphabet values from all states.')

        if current_state in self.accepting_states:
            return True

        return False
