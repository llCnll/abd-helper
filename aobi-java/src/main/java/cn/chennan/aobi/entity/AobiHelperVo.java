package cn.chennan.aobi.entity;

/**
 * @author cn
 * @date 2022-09-17 23:11
 */
public class AobiHelperVo {
    private int businessid;
    private long timestamp;

    public int getBusinessid() {
        return businessid;
    }

    public void setBusinessid(int businessid) {
        this.businessid = businessid;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }

    @Override
    public String toString() {
        return "AobiHelperVo{" +
                "businessid=" + businessid +
                ", timestamp=" + timestamp +
                '}';
    }
}
