package cn.chennan.aobi.controller;

import cn.chennan.aobi.entity.AobiHelperVo;
import com.google.common.collect.Maps;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

/**
 * @author cn
 * @date 2022-09-17 23:01
 */
@RestController
public class AobiHelperController {
    private static final Logger logger = LoggerFactory.getLogger(AobiHelperController.class);

    @PostMapping("/netver/webapi")
    public Map<String, Object> fake(@RequestBody AobiHelperVo vo) {
        logger.info("{}", vo);
        String data;
        if (vo.getBusinessid() == 1) {
            data = String.format("{\"inisoftkey\":\"e8ce98c75b597cc269b41da2e6894eb9b5655fb25755157349ec899a3136e01f1f94ae7e666d53d1f54ff4b9d437d76e8d9cbb6f6c93dd3ba23e58e9d0783e6863658d1a733fb49ee35f185dad7d74b65b4d15f8a96a2471\",\"softinfo\":{\"softname\":\"奥比岛小助手\",\"consultwebsite\":\"\",\"consultqq\":\"\",\"consultwx\":\"\",\"consulttel\":\"\",\"opentestcount\":0,\"opentestday\":0,\"logourl\":\"\",\"notice\":\"\",\"basedata\":\"\",\"newversionnum\":\"\",\"networkdiskurl\":\"\",\"diskpwd\":\"\",\"isforceupd\":0,\"logintypeid\":0,\"consumetypeid\":0,\"isoutsoftuser\":0,\"isbinding\":0,\"deductionconsumevalue\":120,\"maxloginnum\":50},\"softpricelist\":[{\"priceid\":\"e924742ce3aa9819\",\"pricetypename\":\"试用\",\"consumevalue\":1,\"consumeunit\":\"天\",\"price\":0.1,\"roleid\":\"\",\"rolename\":\"\",\"maxLoginNum\":0},{\"priceid\":\"ee8de11adc4e4b99\",\"pricetypename\":\"周版\",\"consumevalue\":1,\"consumeunit\":\"周\",\"price\":0.1,\"roleid\":\"\",\"rolename\":\"\",\"maxLoginNum\":0},{\"priceid\":\"d93ad24489e8e5ca\",\"pricetypename\":\"月卡\",\"consumevalue\":1,\"consumeunit\":\"月\",\"price\":19.9,\"roleid\":\"\",\"rolename\":\"\",\"maxLoginNum\":0},{\"priceid\":\"5a2fca35450b2a60\",\"pricetypename\":\"月版\",\"consumevalue\":1,\"consumeunit\":\"月\",\"price\":100.0,\"roleid\":\"\",\"rolename\":\"\",\"maxLoginNum\":0},{\"priceid\":\"56040b6788cb3620\",\"pricetypename\":\"年卡\",\"consumevalue\":1,\"consumeunit\":\"年\",\"price\":39.9,\"roleid\":\"\",\"rolename\":\"\",\"maxLoginNum\":0},{\"priceid\":\"2deb1bfe8330b209\",\"pricetypename\":\"年版\",\"consumevalue\":1,\"consumeunit\":\"年\",\"price\":29.9,\"roleid\":\"\",\"rolename\":\"\",\"maxLoginNum\":0}],\"requestflag\":\"%s\",\"servertimestamp\":%s}",
                    vo.getTimestamp(), vo.getTimestamp());
        } else if (vo.getBusinessid() == 4) {
            data = String.format("{\"heartbeatkey\":\"bbd6f1ad95a4931d\",\"token\":\"569fdbb26f8ecfa6\",\"endtime\":\"2025-09-18 11:11:11\",\"surpluspointvalue\":0,\"currentloginnum\":1,\"priceid\":\"56040b6788cb3620\",\"pricename\":\"年卡\",\"roleid\":\"\",\"rolename\":\"\",\"maxloginnum\":0,\"ispay\":1,\"jurisdictionlist\":[],\"qq\":\"\",\"wx\":\"\",\"alipay\":\"\",\"tel\":\"\",\"email\":\"\",\"remarks\":\"\",\"requestflag\":\"%s\",\"servertimestamp\":%s}",
                    vo.getTimestamp(), vo.getTimestamp());
        } else {
            data = String.format("{\"heartbeatkey\":\"bbd6f1ad95a4931d\",\"endtime\":\"2025-09-18 11:11:11\",\"surpluspointvalue\":0,\"requestflag\":\"%s\",\"servertimestamp\":%s}",
                    vo.getTimestamp(), vo.getTimestamp());
        }

        Map<String, Object> result = Maps.newHashMap();
        result.put("code", 0);
        result.put("msg", "成功");
        result.put("data", data);
        return result;
    }
}
