% Following program is used to estimate entropies of Corona Virus, Version 2.0
% Contributed to Matlab File Exchange Server, Jun Steed Huang on 10/12/2020
% Jun Steed Huang email: steed.huang@visionx.org     
% The virus gene is calculated from individual measurements:
% https://www.researchgate.net/publication/233914903_Full_genome_analysis_of_a_novel_type_II_feline_coronavirus_NTU156

% Clear the work space
  clear;
  clc;
  clf;
% Input corona virus consensus data for Dog ... human
  d = load('human.txt');      
% Calculate the length of the gene data
  num_data_half = round(size(d)/2);    
% Calculate the non-ergotic entropies for the consensus
% Calculate each point of the graph one by one
        for i=1:num_data_half
            coEmbed(i) = corr(d,circshift(d,i));
            coDim(i) = log(abs(coEmbed(i)))/log(i+1);
        end
  % Plot the correlation map and original censensus respectively
  figure(1);
  plot(coEmbed);
  grid on;
  title('Corora Virus Correlation Diagram');
  xlabel('Gene Sequence 10:1');
  ylabel('Self Correlation');
  figure(2); 
  plot(d); 
  grid on;
  title('Corora Virus Consensus Beijing over Wuhan');
  xlabel('Gene Sequence 10:1');
  ylabel('Consensus');

% Here are dynamic entropy numbers we looking for!
  k = 1;
  dSen = diff(coEmbed);  
        for j=1:num_data_half-1
            if dSen(j)>0;
               alpha(k) = j;
               k = k+1;
            end
        end
  alphaMa = max(alpha);
  alphaMi = min(alpha);
  % Sensitivity to the initial conditions
  qSen = sqrt(alphaMa/alphaMi)-1 % Norm 2 version 2
  % qSen = (alphaMa/alphaMi)-1 % Norm 1 version 1  
  alphaMe = mean(alpha);
  alphaSt = std(alpha);
  % Relaxation process
  qRel = (alphaMe+alphaSt)/(alphaMe-alphaSt)-1
  
% Here is the static entropy number we looking for!
  hStat = hist(d);
  pStat = hStat/sum(hStat);
  % Equilibrium of Einstein Smoluchowski diffusion
  qStat = -sum(pStat.*log(pStat)) 
% Here is the self organized dimmension number we looking for!  
  entrDim = -mean(coDim)*2+1  
% Pictures here
figure(1);
 legend('Self Organized Correlation');   
figure(2); 
 legend('Corona Virus Gene');     