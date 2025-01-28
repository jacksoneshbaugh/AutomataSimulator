from automata import DFATransition


class DFAState:
    """
    Represents the state of an automaton.
    """
    def __init__(self, label: str, transitions: list[DFATransition]):
        """
        Initializes a new state.
        :param label: the label of the state.
        :param transitions: the list of transitions originating in this state.
        """
        self.label = label
        self.transitions = transitions

    def transition(self, label: chr) -> DFATransition:
        """
        Returns the transition corresponding to the given label and this state.
        :param label: the label of the desired transition.
        :return: the transition corresponding to the given label and this state, or None if no transition exists.
        """
        for transition in self.transitions:
            if transition.label == label:
                return transition

        return None
