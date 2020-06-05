FinancialData<-read.csv("ZC=F.csv",row.names=1)
F_data<-ts(FinancialData$Close,start=c(1999,12,21))
plot(F_data)
plot(log(F_data))
acf(diff(log(F_data),5,1),plot=FALSE)

