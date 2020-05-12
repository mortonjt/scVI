import torch

from scvi.dataset import GeneExpressionDataset
from scvi.inference import UnsupervisedTrainer
from scvi.models import VAE, LDVAE

use_cuda = torch.cuda.is_available()


def unsupervised_training_one_epoch(dataset: GeneExpressionDataset):
    vae = VAE(dataset.nb_genes, dataset.n_batches, dataset.n_labels)
    trainer = UnsupervisedTrainer(vae, dataset, train_size=0.5, use_cuda=use_cuda)
    trainer.train(n_epochs=1)

def unsupervised_nb_training_one_epoch(dataset: GeneExpressionDataset):
    vae = LDVAE(dataset.nb_genes, dataset.n_batches, dataset.n_labels, reconstruction_loss = "nb")
    trainer = UnsupervisedTrainer(vae, dataset, train_size=0.5, use_cuda=use_cuda)
    trainer.train(n_epochs=1)
