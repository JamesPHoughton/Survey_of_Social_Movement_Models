import networkx as nx

class ThresholdModel(object):

    def __init__(self, g, fractional_threshold=None, numerical_threshold=None):
        """
        Parameters
        ----------
        g: networkx graph
        fractional_threshold: list of numbers
            these are values between 0 and 1 representing the fraction of the neighbors who need
            to be activated before the focal node will become activated.
            For these thresholds, adopters are
        numerical_threshold: list of integers
            these are
            This innovation from Centola and Macy 2007


        """
        self.g = g
        if fractional_threshold:
            fractional_threshold_dict = dict(zip(g.nodes(), fractional_threshold))
            nx.set_node_attributes(self.g, 'fractional threshold', fractional_threshold_dict)
        else:
            nx.set_node_attributes(self.g, 'fractional threshold', 0)

        if numerical_threshold:
            numerical_threshold_dict = dict(zip(g.nodes(), numerical_threshold))
            nx.set_node_attributes(self.g, 'numerical threshold', numerical_threshold_dict)
        else:
            nx.set_node_attributes(self.g, 'numerical threshold', 0)


        nx.set_node_attributes(self.g, 'adopting', False)
        #g.node[g.nodes()[0]]['threshold'] = 0

    def seed(self):

    def draw(self):
        key = {False: 'b', True: 'r'}
        colors = [key[self.g.node[n]['adopting']] for n in self.g.nodes()]
        nx.draw_circular(self.g, alpha=.6, node_color=colors)

    def step(self):
        def decide(g, n):
            neighbors = g.neighbors(n)
            threshold = g.node[n]['threshold']
            rioting = sum([g.node[neighbor]['adopting'] for neighbor in neighbors])
            return rioting >= (threshold * len(neighbors))

        new_state = dict(zip(self.g.nodes(), [decide(self.g, n) for n in self.g.nodes()]))
        nx.set_node_attributes(self.g, 'adopting', new_state)

    def num_rioting(self):
        return sum([self.g.node[n]['rioting'] for n in self.g.nodes()])