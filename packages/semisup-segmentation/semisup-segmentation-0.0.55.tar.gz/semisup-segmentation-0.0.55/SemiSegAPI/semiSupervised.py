from SemiSegAPI.utils import *
from fastai.vision.all import *
import shutil
import os

def dataDistillation(baseModel, baseBackbone, targetModel, targetBackbone, transforms, path, pathUnlabelled, outputPath, bs=32, size=(480,640)):
    if not testNameModel(baseModel):
        print("The base model selected is not valid")
    elif not testNameModel(targetModel):
        print("The target model selected is not valid")
    elif not testPath(path):
        print("The path is invalid or has an invalid structure")
    elif not testTransforms(transforms):
        print("There are invalid transforms")
    else:
        # Load images
        dls = get_dls(path, size, bs=bs)
        nClasses=numClasses(path)

        learn = getLearner(baseModel,baseBackbone,nClasses,path,dls)

        # Train base learner
        print("Start of base model training")
        train_learner(learn, 50, freeze_epochs=2)
        learn.save(baseModel)

        if not os.path.exists(outputPath):
            os.makedirs(outputPath)
        shutil.copy(path + os.sep + 'models' + os.sep + baseModel + '.pth',
                    outputPath + os.sep + 'base_' + baseModel + '.pth')

        # supervised method
        print("Start of annotation")
        omniData(path, pathUnlabelled, learn, transforms,size)
        print("End of annotation")

        # Load new images
        dls2 = get_dls(path, size, bs=bs)

        # Load base model
        learn2 = getLearner(targetModel, targetBackbone, nClasses, path, dls2)

        # Train base learner
        print("Start of target model training")
        train_learner(learn2, 50, freeze_epochs=2)
        learn2.save(targetModel)
        shutil.copy(path + '_tmp' + os.sep + 'models' + os.sep + targetModel + '.pth',
                    outputPath + os.sep + 'target_' + targetModel + '.pth')
        shutil.rmtree(path + '_tmp')


def modelDistillation(baseModels, baseBackbones, targetModel, targetBackbone, path, pathUnlabelled, outputPath, bs=32, size=224, confidence=0.8):
    for baseModel in baseModels:
        if not testNameModel(baseModel):
            print("The base model selected is not valid")
            return
    if not testNameModel(targetModel):
        print("The target model selected is not valid")
    elif not testPath(path):
        print("The path is invalid or has an invalid structure")
    else:
        # Load images

        nClasses = numClasses(path)
        if nClasses > 1:
            metric = [Dice()]
        else:
            metric = [DiceMulti()]

        # Load base model
        learners=[]
        print("Start of base models training")
        for baseModel, i in enumerate(baseModels):
            dls = get_dls(path, size, bs=bs)
            bModel = getModel(baseModel, baseBackbones[i], nClasses)

            # Create base learner
            save = SaveModelCallback(monitor='valid_loss', fname='model-' + baseModel)
            early = EarlyStoppingCallback(monitor='valid_loss', patience=5)
            learn = Learner(dls, bModel, metrics=metric, cbs=[early, save], path=path)

            # Train base learner
            train_learner(learn, 50, freeze_epochs=2)
            # learn.fine_tune(50, freeze_epochs=2)
            learn.save(baseModel)
            if not os.path.exists(outputPath):
                os.makedirs(outputPath)
            shutil.copy(path + os.sep + 'models' + os.sep + baseModel + '.pth',
                        outputPath + os.sep + 'base_' + baseModel + '.pth')
            learners.append(learn)


        # supervised method
        print("Start of annotation")
        omniModel(path, pathUnlabelled, learners,size)
        print("End of annotation")

        # Load new images
        dls2 = get_dls(path, size, bs=bs)

        # Load base model
        tModel = getModel(targetModel, targetBackbone, nClasses)

        # Create base learner
        save2 = SaveModelCallback(monitor='valid_loss', fname='model-' + targetModel)
        early2 = EarlyStoppingCallback(monitor='valid_loss', patience=5)
        learn2 = Learner(dls2, tModel, metrics=metric, cbs=[early2, save2], path=path)

        # Train base learner
        print("Start of target model training")
        train_learner(learn2, 50, freeze_epochs=2)
        # learn2.fine_tune(50, freeze_epochs=2)
        learn2.save(targetModel)
        shutil.copy(path + '_tmp' + os.sep + 'models' + os.sep + targetModel + '.pth',
                    outputPath + os.sep + 'target_' + targetModel + '.pth')
        shutil.rmtree(path + '_tmp')


def modelDataDistillation(baseModels, baseBackbones, targetModel, targetBackbone, transforms, path, pathUnlabelled, outputPath, bs=32, size=224, confidence=0.8):
    for baseModel in baseModels:
        if not testNameModel(baseModel):
            print("The base model selected is not valid")
            return
    if not testNameModel(targetModel):
        print("The target model selected is not valid")
    elif not testPath(path):
        print("The path is invalid or has an invalid structure")
    elif not testTransforms(transforms):
        print("There are invalid transforms")
    else:
        nClasses = numClasses(path)
        if nClasses > 1:
            metric = [Dice()]
        else:
            metric = [DiceMulti()]
        # Load images
        learners=[]
        print("Start of base models training")
        for baseModel in baseModels:
            dls = get_dls(path, size, bs=bs)
            bModel = getModel(baseModel, baseBackbones[i], nClasses)

            # Create base learner
            save = SaveModelCallback(monitor='valid_loss', fname='model-' + baseModel)
            early = EarlyStoppingCallback(monitor='valid_loss', patience=5)
            learn = Learner(dls, bModel, metrics=metric, cbs=[early, save], path=path)

            # Train base learner
            train_learner(learn, 50, freeze_epochs=2)
            # learn.fine_tune(50, freeze_epochs=2)
            learn.save(baseModel)
            if not os.path.exists(outputPath):
                os.makedirs(outputPath)
            shutil.copy(path + os.sep + 'models' + os.sep + baseModel + '.pth',
                        outputPath + os.sep + 'base_' + baseModel + '.pth')
            learners.append(learn)

        # supervised method
        print("Start of annotation")
        omniModelData(path, pathUnlabelled, learners, transforms,size)
        print("End of annotation")

        # Load new images
        dls2 = get_dls(path, size, bs=bs)

        # Load base model
        tModel = getModel(targetModel, targetBackbone, nClasses)

        # Create base learner
        save2 = SaveModelCallback(monitor='valid_loss', fname='model-' + targetModel)
        early2 = EarlyStoppingCallback(monitor='valid_loss', patience=5)
        learn2 = Learner(dls2, tModel, metrics=metric, cbs=[early2, save2], path=path)

        # Train base learner
        print("Start of target model training")
        train_learner(learn2, 50, freeze_epochs=2)
        # learn2.fine_tune(50, freeze_epochs=2)
        learn2.save(targetModel)
        shutil.copy(path + '_tmp' + os.sep + 'models' + os.sep + targetModel + '.pth',
                    outputPath + os.sep + 'target_' + targetModel + '.pth')
        shutil.rmtree(path + '_tmp')

def simpleTraining(baseModel, baseBackbone, path, outputPath, bs=32, size=224):
    if not testNameModel(baseModel):
        print("The base model selected is not valid")
    elif not testPath(path):
        print("The path is invalid or has an invalid structure")
    else:
        # Load images
        dls = get_dls(path, size, bs=bs)
        nClasses = numClasses(path)
        if nClasses > 1:
            metric = [Dice()]
        else:
            metric = [DiceMulti()]

        # Load base model
        bModel = getModel(baseModel, baseBackbone, nClasses)

        # Create base learner
        save = SaveModelCallback(monitor='valid_loss', fname='model-' + baseModel)
        early = EarlyStoppingCallback(monitor='valid_loss', patience=5)
        learn = Learner(dls, bModel, metrics=metric, cbs=[early, save], path=path)

        # Train base learner
        print("Start of model training")
        train_learner(learn, 50, freeze_epochs=2)
        # learn.fine_tune(50, freeze_epochs=2)
        learn.save(baseModel)
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)
        shutil.copy(path+os.sep+'models'+os.sep+baseModel+'.pth',outputPath+os.sep+'target_'+baseModel+'.pth')
