import numpy as np
import matplotlib.pyplot as plt
from satellite_analysis.massrelations import stellarmass_relations
from scipy.stats import chisquare

def centralandsatellitegalaxypapercomparisons(darkmattermasscentral, stellarmasscentral, massratiocentral, darkmattermasssatellite, stellarmasssatellite, massratiosatellite, Behroozirelation, Pueblarelation, x, output_dir, a, title):
    plt.figure(1, figsize=(20,10))
    plt.subplot(121)
    plt.title('Scale Factor %s' % str(a/1000))
    plt.xlabel('halomass')
    plt.ylabel('massratio')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(10**(7.8), 10**(14))
    #plt.ylim(0.0, 0.10)
    plt.plot(x, Behroozirelation[3], 'k', color='#CC4F1B')
    plt.plot(x, Pueblarelation[3], 'k', color='#1B2ACC')
    plt.scatter(darkmattermasscentral, massratiocentral, s = 1)
    plt.scatter(darkmattermasssatellite, massratiosatellite, s = 1, c = 'r')
    plt.fill_between(x, Behroozirelation[5], Behroozirelation[4], alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    plt.fill_between(x, Pueblarelation[5], Pueblarelation[4], alpha=0.5, edgecolor='#1B2ACC', facecolor='#089FFF')
    plt.legend(('Behroozi2013', 'Rodriguez-Puebla2017', 'Host Galaxies', 'Satellite Galaxies'))
    
    plt.subplot(122)
    plt.xlabel('halomass')
    plt.ylabel('stellarmass')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(10**(7.8), 10**(14))
    plt.ylim(10**(-2), 10**(14))
    plt.plot(x, 10**Behroozirelation[0], 'k', color='#CC4F1B')
    plt.fill_between(x, 10**Behroozirelation[2], 10**Behroozirelation[1], alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    plt.plot(x, 10**Pueblarelation[0], 'k', color='#1B2ACC')
    plt.fill_between(x, 10**Pueblarelation[2], 10**Pueblarelation[1], alpha=0.5, edgecolor='#1B2ACC', facecolor='#089FFF')
    plt.scatter(darkmattermasscentral, stellarmasscentral, s = 1)
    plt.scatter(darkmattermasssatellite, stellarmasssatellite, s = 1, c = 'r')
    plt.savefig('%s/hostsandsatellites%s%s.png' % (output_dir, title, str(a)))
    plt.close()

def satellitegalaxypapercomparisons(darkmattermass, stellarmass, massratio, Behroozirelation, Pueblarelation, x, output_dir, a, title):
    plt.figure(1, figsize=(20,10))
    plt.subplot(121)
    plt.title('Scale Factor %s' % str(a/1000))
    plt.xlabel('halomass')
    plt.ylabel('massratio')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(10**(7.8), 10**(14))
    #plt.ylim(0.0, 0.10)
    plt.plot(x, Behroozirelation[3], 'k', color='#CC4F1B')
    plt.plot(x, Pueblarelation[3], 'k', color='#1B2ACC')
    plt.scatter(darkmattermass, massratio, s = 1, c = 'r')
    plt.fill_between(x, Behroozirelation[5], Behroozirelation[4], alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    plt.fill_between(x, Pueblarelation[5], Pueblarelation[4], alpha=0.5, edgecolor='#1B2ACC', facecolor='#089FFF')
    plt.legend(('Behroozi2013', 'Rodriguez-Puebla2017', 'Satellite Galaxies'))
    
    plt.subplot(122)
    plt.xlabel('halomass')
    plt.ylabel('stellarmass')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(10**(7.8), 10**(14))
    plt.ylim(10**(-2), 10**(14))
    plt.plot(x, 10**Behroozirelation[0], 'k', color='#CC4F1B')
    plt.fill_between(x, 10**Behroozirelation[2], 10**Behroozirelation[1], alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    plt.plot(x, 10**Pueblarelation[0], 'k', color='#1B2ACC')
    plt.fill_between(x, 10**Pueblarelation[2], 10**Pueblarelation[1], alpha=0.5, edgecolor='#1B2ACC', facecolor='#089FFF')
    plt.scatter(darkmattermass, stellarmass, s = 1, c = 'r')
    plt.savefig('%s/satellites%s%s.png' % (output_dir, title, str(a)))
    plt.close()

def centralgalaxypapercomparisons(darkmattermass, stellarmass, massratio, Behroozirelation, Pueblarelation, x, output_dir, a, title):
    plt.figure(1, figsize=(20,10))
    plt.subplot(121)
    plt.title('Scale Factor %s' % str(a/1000))
    plt.xlabel('halomass')
    plt.ylabel('massratio')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(10**(7.8), 10**(14))
    #plt.ylim(0.0, 0.10)
    plt.plot(x, Behroozirelation[3], 'k', color='#CC4F1B')
    plt.plot(x, Pueblarelation[3], 'k', color='#1B2ACC')
    plt.scatter(darkmattermass, massratio, s = 1)
    plt.fill_between(x, Behroozirelation[5], Behroozirelation[4], alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    plt.fill_between(x, Pueblarelation[5], Pueblarelation[4], alpha=0.5, edgecolor='#1B2ACC', facecolor='#089FFF')
    plt.legend(('Behroozi2013', 'Rodriguez-Puebla2017', 'Host Galaxies'))
    
    plt.subplot(122)
    plt.xlabel('halomass')
    plt.ylabel('stellarmass')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(10**(7.8), 10**(14))
    plt.ylim(10**(-2), 10**(14))
    plt.plot(x, 10**Behroozirelation[0], 'k', color='#CC4F1B')
    plt.fill_between(x, 10**Behroozirelation[2], 10**Behroozirelation[1], alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    plt.plot(x, 10**Pueblarelation[0], 'k', color='#1B2ACC')
    plt.fill_between(x, 10**Pueblarelation[2], 10**Pueblarelation[1], alpha=0.5, edgecolor='#1B2ACC', facecolor='#089FFF')
    plt.scatter(darkmattermass, stellarmass, s = 1)
    plt.savefig('%s/hosts%s%s.png' % (output_dir, title, str(a)))
    plt.close()