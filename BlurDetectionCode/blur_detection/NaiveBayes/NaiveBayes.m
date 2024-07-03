classdef NaiveBayes
    properties
        data
    end

    methods (Static)
        function obj = loadobj(nb)
           obj = NaiveBayes;
           obj.data = nb;
        end
    end
end