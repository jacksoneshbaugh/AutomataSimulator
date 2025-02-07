<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>
# AutomataSimulator
Modeling automata defined in `json` files

## 1. About
As I began my Spring 2025 semester at Lafayette College, I embarked on a new quest: _CS 303: Theory of Computation_. As I began my first assignment (designing DFA), I wanted a tool that could emulate the theoretical machines I was tasked with constructing. So, I created this program, which I hope to update as I progress through the course (i.e., add other types of automata to the tool). I hope it is useful to you!

## 2. Using AutomataSimulator

### 2.1 Deterministic Finite Automata
> According to Michael Sipser in _Introduction to the Theory of Computation, Third Edition_, A finite automaton is a 5-tuple M = $(Q, \Sigma, \delta, q_0, F)$, where:
> 1. $Q$ is a finite set of **states**,
> 2. $\Sigma$ is a finite set called the **alphabet**,
> 3. $\delta: Q \cross \Sigma \rarrow Q$ is the **transition function**,
> 4. $q_0 \in Q$ is the **start state**, and
> 5. $F \subset Q$ is the **set of accept states**.

We define these same properties in `json`.

1. `type`—the type of machine this file represents. I will update this tool to support more types of theoretical machines, but for now only `deterministic_finite_automaton` is a supported type.
2. `alphabet`—the alphabet ($\Sigma$) of the theoretical machine.
3. `states`—a list of states in the machine. Each state is defined with a `label` and a list of `transitions`. See an example:
```json
{
  "label": "q0",
  "transitions": [
    {"label": "0", "to_state": "q1"},
    {"label": "1", "to_state": "q0"}
  ]
}
```
4. `initial_state`—the state at which the automaton begins
5. `accepting_states`—the list of accepting states

```json
{
  "type": "deterministic_finite_automaton",
  "alphabet": ["0", "1"],
  "states": [
    {
      "label": "q0",
      "transitions": [
        {"label": "0", "to_state": "q1"},
        {"label": "1", "to_state": "q0"}
      ]
    },
    {
      "label": "q1",
      "transitions": [
        {"label": "0", "to_state": "q2"},
        {"label": "1", "to_state": "q0"}
      ]
    },
    {
      "label": "q2",
      "transitions": [
        {"label": "0", "to_state": "q2"},
        {"label": "1", "to_state": "q3"}
      ]
    },
    {
      "label": "q3",
      "transitions": [
        {"label": "0", "to_state": "q3"},
        {"label": "1", "to_state": "q3"}
      ]
    }
  ],
  "initial_state": "q0",
  "accepting_states": ["q0", "q1", "q2"]
}
```

Once you have the `json` file, simply run the program and follow the prompts.

### 2.2: Nondeterministic Finite Automata
To run NFAs, just change the `type` to ```json "type": "nondeterministic_finite_automaton"```. Also, as a note: $\epsilon$ is denoted as "" here.

## 3. About Me
My name is Jackson Eshbaugh, and I'm a computer science/French student at Lafayette College interested in the overlaps that computer science makes with other fields of study. I'm excited about fields like bioinformatics (computational biology) and computational linguistics. Please check out my [website at https://jacksoneshbaugh.github.io](https://jacksoneshbaugh.github.io)!