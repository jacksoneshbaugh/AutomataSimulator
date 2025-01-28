from automata import DFAState


class DFATransition:
    """
    Represents a transition in a deterministic finite automaton.
    """
    def __init__(self, label: chr, state: DFAState):
        """
        Initializes a new transition.
        :param label: The label of the transition.
        :param state: the state that this transition will lead to.
        """
        self.label = label
        self.state = state
