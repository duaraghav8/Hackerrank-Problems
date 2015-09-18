#PYTHON 2
from pybrain.structure import FeedForwardNetwork;
from pybrain.structure import LinearLayer, SigmoidLayer;
from pybrain.structure import FullConnection as FConnect;
from pybrain.datasets.supervised import SupervisedDataSet as DataSet;
from pybrain.supervised.trainers import BackpropTrainer;

def getTrainingData ():
	trainingData = [];
	for line in open ('trainingdata.txt', 'r'):
		trainingData.append ([float (i) for i in line.split (',')]);

	return (trainingData);

if (__name__) == '__main__':
	trainingData = getTrainingData ();
	network = FeedForwardNetwork ();

	inputLayer = LinearLayer (1);
	hiddenLayer = SigmoidLayer (3);
	outputLayer = LinearLayer (1);

	inToMid = FConnect (inputLayer, hiddenLayer);
	midToOut = FConnect (hiddenLayer, outputLayer);
	data = DataSet (1, 1);

	network.addInputModule (inputLayer);
	network.addModule (hiddenLayer);
	network.addOutputModule (outputLayer);

	network.addConnection (inToMid);
	network.addConnection (midToOut);
	network.sortModules ();

	for item in trainingData:
		data.addSample ( (item [0], ), (item [1], ) );

	trainer = BackpropTrainer (network, dataset=data, momentum=0.1, verbose=True, weightdecay=0.01);
	trainer.train ();
